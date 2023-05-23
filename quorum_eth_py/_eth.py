import logging

from quorum_mininode_py import create_pvtkey
from web3 import Web3
from web3.middleware import geth_poa_middleware

from quorum_eth_py._constants import RUM_ETH_CHAINID, RUM_ETH_HTTP_PROVIDER
from quorum_eth_py.contract.PaidGroupV2 import abi as PaidGroup_abiv2
from quorum_eth_py.contract.PaidGroupV2 import bytecode as PaidGroup_bytecodev2
from quorum_eth_py.contract.RumERC20 import abi as RumERC20_abi
from quorum_eth_py.contract.RumERC20 import bytecode as RumERC20_bytecode

logger = logging.getLogger(__name__)


class RumEthChain:
    """https://github.com/rumsystem/rum-eth-mvm/blob/main/RUM-ETH.md"""

    def __init__(self, pvtkey: str = None):
        pvtkey = pvtkey or create_pvtkey()
        self.w3 = Web3(Web3.HTTPProvider(RUM_ETH_HTTP_PROVIDER))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.is_connected()
        self.account = self.w3.eth.account.from_key(pvtkey)
        self.w3.eth.default_account = self.account.address
        logger.info("account address: %s", self.account.address)

    def is_connected(self):
        status = self.w3.is_connected()
        logger.info("connected to rum-eth-chain: %s", status)
        return status

    def get_balance(self, address: str = None):
        """get the balance of address, default is the account address"""
        address = address or self.account.address
        address = self.w3.to_checksum_address(address)
        balance_wei = self.w3.eth.get_balance(address)
        balance = self.w3.from_wei(balance_wei, "ether")
        return balance

    def send_transction(self, trx: dict):
        signed_trx = self.w3.eth.account.sign_transaction(
            trx, private_key=self.account.key
        )
        trx_hash = self.w3.eth.send_raw_transaction(signed_trx.rawTransaction)
        trx_receipt = self.w3.eth.wait_for_transaction_receipt(trx_hash)

        tid = self.get_trx_id(trx_receipt)
        if trx_receipt["status"] == 1:
            logger.info("send_transction success: %s", tid)
        else:
            logger.error("send_transction failed: %s", tid)
        return trx_receipt

    def init_gas_options(self, to: str = None, value: float = None, gas: int = 10000):
        """init gas options"""
        options = {
            "from": self.account.address,
            "nonce": self.w3.eth.get_transaction_count(self.account.address),
            "gasPrice": self.w3.to_wei("1", "gwei"),
            "gas": gas,
            "chainId": RUM_ETH_CHAINID,
        }
        if to:
            options.update({"to": self.w3.to_checksum_address(to)})
        if value:
            options.update({"value": self.w3.to_wei(value, "ether")})
            if self.get_balance() < value:
                raise Exception(f"balance not enough {self.get_balance()}")

        gas_limit = self.w3.eth.estimate_gas(options) + 5000
        if gas_limit > options["gas"]:
            options["gas"] = gas_limit
        logger.info("gas options: %s", options["gas"])

        if self.get_balance() < self.w3.from_wei(options["gas"], "ether"):
            raise Exception(f"not enough for gas fee {self.get_balance()}")

        return options

    def transfer(self, to_address: str, num: float):
        """transfer rum to address, the rum is origin token of poa chain, used as gas feed"""
        # check balance of account
        if num <= 0:
            raise Exception("transfer num must be positive")
        to_address = self.w3.to_checksum_address(to_address)
        options = self.init_gas_options(to=to_address, value=num)
        return self.send_transction(options)

    def get_trx(self, tx_id_hex: str):
        receipt = self.w3.eth.get_transaction_receipt(tx_id_hex)
        return receipt

    def get_trx_id(self, tx_receipt):
        return tx_receipt.transactionHash.hex()

    def contract_instance(self, contract_address, abi):
        return self.w3.eth.contract(contract_address, abi=abi)

    def deploy_erc20(
        self,
        name: str,
        symbol: str,
        total_supply: int,
        minter_address: str = None,
        abi=RumERC20_abi,
        bytecode=RumERC20_bytecode,
    ):
        """deploy new erc20 contract"""
        contract = self.w3.eth.contract(abi=abi, bytecode=bytecode)
        options = self.init_gas_options(gas=2000000)
        con = contract.constructor(
            cap=self.w3.to_wei(total_supply, "ether"),
            name_=name,
            symbol_=symbol,
            minter=self.w3.to_checksum_address(minter_address or self.account.address),
        )
        _gas = con.estimate_gas() + 10000
        if _gas > options["gas"]:
            logger.info("gas options: %s → %s", options["gas"], _gas)
            options["gas"] = _gas
        receipt = self.send_transction(con.build_transaction(options))
        logger.info("deploy erc20 contract success: %s", receipt.contractAddress)
        return receipt

    def deploy_paidgroup_v2(
        self,
        name: str,
        receive_addr: str,
        invoke_fee: float = 0.001,
        share_ratio=95,
        version: str = "0.1.0",
        abi=PaidGroup_abiv2,
        bytecode=PaidGroup_bytecodev2,
    ):
        # deploy contract
        pg = self.w3.eth.contract(abi=abi, bytecode=bytecode)
        payload = (
            version,
            self.w3.to_wei(invoke_fee, "ether"),
            share_ratio,
            receive_addr,
            name,
            self.account.address,
        )
        options = self.init_gas_options()
        con = pg.constructor(*payload)
        _gas = con.estimate_gas() + 10000
        if _gas > options["gas"]:
            options["gas"] = _gas
        receipt = self.send_transction(con.build_transaction(options))
        # init contract
        pg = self.contract_instance(receipt.contractAddress, abi)
        options = self.init_gas_options(gas=3500000)
        init = pg.functions.initialize(*payload)
        _gas = init.estimate_gas() + 10000
        if _gas > options["gas"]:
            options["gas"] = _gas
        self.send_transction(init.build_transaction(options))
        return receipt
