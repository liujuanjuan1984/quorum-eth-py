import logging

from quorum_eth_py._eth import RumEthChain
from quorum_eth_py.contract.RumERC20 import abi as RumERC20_abi

logger = logging.getLogger(__name__)


class RumERC20:
    """
    the contract instance of RumERC20
    https://github.com/rumsystem/rum-eth-mvm/blob/main/dapps/RumERC20/contracts/RumERC20.sol
    """

    def __init__(
        self,
        contract_address: str,
        pvtkey: str = None,
        chain: RumEthChain = None,
        abi=None,
    ):
        self.chain = chain or RumEthChain(pvtkey)
        self.w3 = self.chain.w3
        self.account = self.chain.account
        _addr = self.w3.to_checksum_address(contract_address)
        self.erc20 = self.chain.contract_instance(_addr, abi or RumERC20_abi)
        self.funcs = self.erc20.functions

    def name(self):
        return self.funcs.name().call()

    def symbol(self):
        return self.funcs.symbol().call()

    def decimals(self):
        return self.funcs.decimals().call()

    def total_supply(self):
        unit256 = self.funcs.totalSupply().call()
        return self.w3.from_wei(unit256, "ether")

    def get_balance(self, address: str = None):
        address = self.w3.to_checksum_address(address or self.account.address)
        unit256 = self.funcs.balanceOf(address).call()
        return self.w3.from_wei(unit256, "ether")

    def get_rum_balance(self, address: str = None):
        return self.chain.get_balance(address or self.account.address)

    def transfer(self, to_address: str, num: float):
        """transfter num of token to address"""
        to_address = self.w3.to_checksum_address(to_address)
        options = self.chain.init_gas_options()
        tx = self.funcs.transfer(
            to_address, self.w3.to_wei(num, "ether")
        ).build_transaction(options)
        return self.chain.send_transction(tx)

    def approve(self, to_address: str, num: float):
        to_address = self.w3.to_checksum_address(to_address)
        options = self.chain.init_gas_options()
        tx = self.funcs.approve(
            to_address, self.w3.to_wei(num, "ether")
        ).build_transaction(options)
        return self.chain.send_transction(tx)
