import logging
import struct
import uuid
from dataclasses import dataclass

from quorum_eth_py._constants import RUM_PAIDGROUP_ADDRESS
from quorum_eth_py._eth import RumEthChain
from quorum_eth_py._rum_erc20 import RumERC20
from quorum_eth_py.contract.PaidGroupV2 import abi as PaidGroup_abiv2

logger = logging.getLogger(__name__)


@dataclass
class DappInfo:
    name: str
    version: str
    developer: str
    receiver: str  # 平台收款地址
    deployer: str
    invoke_fee: int
    share_ratio: int


@dataclass
class PriceInfo:
    address: str  # group owner
    token_addr: str  # token contract address
    amount: float  # token amount
    duration: int  # duration in seconds


@dataclass
class Member:
    group_id: str
    amount: float
    token_addr: str
    expired_at: int  # expiredAt = duration + paidAt，expiredAt > now 决定没有过期


def int_to_uint64(i):
    b = struct.pack("<Q", i)
    u = int.from_bytes(b, byteorder="little")
    return u


def uuid_to_unit128(uid: str):
    uid = uuid.UUID(uid)
    return int(uid.int)


class PaidGroup:
    """
    the paid group contract instance of rum-eth chain
    https://github.com/rumsystem/rum-eth-mvm/blob/main/dapps/RumPaidGroup/README.md
    """

    def __init__(
        self,
        pvtkey: str = None,
        contract_address: str = None,
        chain: RumEthChain = None,
        abi: str = None,
    ):

        self.chain = chain or RumEthChain(pvtkey)
        self.w3 = self.chain.w3
        self.account = self.chain.account
        _addr = contract_address or RUM_PAIDGROUP_ADDRESS
        _addr = self.w3.to_checksum_address(_addr)
        self.pg = self.chain.contract_instance(_addr, abi or PaidGroup_abiv2)
        self.funcs = self.pg.functions

    def is_equal_string(self, a: str, b: str):
        return self.funcs.isEqualString(a, b).call()

    def get_dapp_info(self):
        info = self.funcs.getDappInfo().call()
        return DappInfo(*info).__dict__

    def update_dapp_info(self, version: str, invoke_fee: int, share_ratio: int):
        # owner only
        if share_ratio <= 0 or share_ratio > 100:
            raise Exception("share_ratio must be between 0 and 100")
        options = self.chain.init_gas_options()
        update = self.funcs.updateDappInfo(version, invoke_fee, share_ratio)
        _gas = update.estimate_gas() + 10000
        if _gas > options["gas"]:
            options["gas"] = _gas
        build_tx = update.build_transaction(options)
        return self.chain.send_transction(build_tx)

    def invoke_fee(self):
        invoke_feed = self.get_dapp_info().get("invoke_fee")
        num = self.w3.from_wei(invoke_feed, "ether")
        logger.info("invoke fee: %s RUM", num)
        return num

    def get_balance(self):
        # owner only TODO:
        return self.funcs.getBalance().call()

    def get_price(self, group_id: str):
        group_id = uuid_to_unit128(group_id)
        info = self.funcs.getPrice(group_id).call()
        price = PriceInfo(*info)
        price.amount = self.w3.from_wei(price.amount, "ether")
        return price.__dict__

    def add_price(self, group_id: str, duration: int, token_addr: str, amount: float):
        """
        group_id: uuid of the group
        duration: duration in seconds # TODO:check it
        token_addr: token contract address
        amount: token amount
        """
        # TODO:durations must be between 1 and 365 days (in seconds)???
        options = self.chain.init_gas_options(gas=200000, value=self.invoke_fee())
        build_tx = self.funcs.addPrice(
            uuid_to_unit128(group_id),
            int_to_uint64(duration),
            self.w3.to_checksum_address(token_addr),
            self.w3.to_wei(amount, "ether"),
        ).build_transaction(options)
        return self.chain.send_transction(build_tx)

    def update_price(
        self, group_id: str, duration: int, token_addr: str, amount: float
    ):
        """
        group_id: uuid of the group
        duration: duration in seconds # TODO:check it
        token_addr: token contract address
        amount: token amount
        """
        options = self.chain.init_gas_options(value=self.invoke_fee(), gas=200000)
        tx = self.funcs.updatePrice(
            uuid_to_unit128(group_id),
            int_to_uint64(duration),
            self.w3.to_checksum_address(token_addr),
            self.w3.to_wei(amount, "ether"),
        ).build_transaction(options)
        return self.chain.send_transction(tx)

    def get_member(self, address: str, group_id: str):
        """get member info of address in group_id"""
        return self.funcs.getMemberKey(
            self.w3.to_checksum_address(address), uuid_to_unit128(group_id)
        ).call()

    def get_paid_detail(self, address: str, group_id: str):
        info = self.funcs.getPaidDetail(
            self.w3.to_checksum_address(address), uuid_to_unit128(group_id)
        ).call()
        member = Member(*info)
        member.amount = self.w3.from_wei(member.amount, "ether")
        return member.__dict__

    def is_paid(self, address: str, group_id: str):
        return self.funcs.isPaid(
            self.w3.to_checksum_address(address), uuid_to_unit128(group_id)
        ).call()

    def pay(self, group_id: str):
        """pay for group_id to the owner"""
        if self.is_paid(self.account.address, group_id):
            return True
        price = self.get_price(group_id)
        erc20 = RumERC20(
            contract_address=price.get("token_addr"),
            pvtkey=self.account.key,
            chain=self.chain,
        )
        if erc20.get_balance() < price.get("amount"):
            raise Exception("not enough balance")
        receipt = erc20.approve(self.pg.address, price.get("amount"))
        if receipt["status"] != 1:
            raise Exception("approve failed")
        logger.info("approve to %s %s", self.pg.address, price.get("amount"))

        options = self.chain.init_gas_options(gas=200000)
        tx = self.funcs.pay(
            uuid_to_unit128(group_id),
        ).build_transaction(options)
        return self.chain.send_transction(tx)
