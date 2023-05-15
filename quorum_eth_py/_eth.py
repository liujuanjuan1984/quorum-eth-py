import asyncio
import logging

from quorum_mininode_py import create_pvtkey
from web3 import Web3
from web3.middleware import geth_poa_middleware

from quorum_eth_py.contract.RumERC20 import abi as RumERC20_abi
from quorum_eth_py.contract.RumERC20 import bytecode as RumERC20_bytecode

logger = logging.getLogger(__name__)


RUM_ETH_HTTP_PROVIDER = "http://149.56.22.113:8545"
RUM_ETH_CHAINID = 19890609


class RumEthChain:
    """https://github.com/rumsystem/rum-eth-mvm/blob/main/RUM-ETH.md"""

    def __init__(self, pvtkey: str = None):
        pvtkey = pvtkey or create_pvtkey()
        self.w3 = Web3(Web3.HTTPProvider(RUM_ETH_HTTP_PROVIDER))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.is_connected()
        self.account = self.w3.eth.account.from_key(pvtkey)
        self.w3.eth.defaultAccount = self.account.address
        logger.info("account address: %s", self.account.address)

    def is_connected(self):
        status = self.w3.isConnected()
        logger.info("connected to rum-eth-chain: %s", status)
        return status

    def get_balance(self, address: str = None):
        """get the balance of address, default is the account address"""
        address = address or self.account.address
        address = self.w3.toChecksumAddress(address)
        balance_wei = self.w3.eth.getBalance(address)
        balance = self.w3.fromWei(balance_wei, "ether")
        return balance

    def _transction(self, tx: dict):
        signed_tx = self.w3.eth.account.sign_transaction(
            tx, private_key=self.account.privateKey
        )
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def transfer(self, to_address: str, num):
        """transfer rum to address, the rum is origin token of poa chain, used as gas feed"""
        # check balance of account
        if num <= 0:
            raise Exception("transfer num must be positive")
        to_address = self.w3.toChecksumAddress(to_address)
        if self.get_balance() < num:
            raise Exception(f"balance not enough {self.get_balance()}")
        tx = {
            "nonce": self.w3.eth.getTransactionCount(self.account.address),
            "to": to_address,
            "value": self.w3.toWei(num, "ether"),
            "gasPrice": self.w3.toWei("10", "gwei"),
            "gas": 50000,
            "chainId": RUM_ETH_CHAINID,
        }
        gas_limit = self.w3.eth.estimateGas(tx)
        if gas_limit > tx["gas"]:
            tx["gas"] = gas_limit
        tx_receipt = self._transction(tx)
        tid = tx_receipt.transactionHash.hex()
        return tid

    def contract_instance(self, abi, contract_address):
        contract_instance = self.w3.eth.contract(contract_address, abi=abi)
        return contract_instance

    def deploy_erc20(
        self, name, symbol, total_supply, minter_address=None, abi=None, bytecode=None
    ):
        """deploy new erc20 contract"""
        abi = abi or RumERC20_abi
        bytecode = bytecode or RumERC20_bytecode
        contract = self.w3.eth.contract(abi=abi, bytecode=bytecode)
        cap = self.w3.toWei(total_supply, "ether")
        minter = self.w3.toChecksumAddress(minter_address or self.account.address)

        tx = {
            "from": self.account.address,
            "nonce": self.w3.eth.getTransactionCount(self.account.address),
            "gasPrice": self.w3.toWei("10", "gwei"),
            "gas": 50000,
            "chainId": RUM_ETH_CHAINID,
        }
        gas_limit = contract.constructor(
            cap=cap, name_=name, symbol_=symbol, minter=minter
        ).estimateGas()
        if gas_limit > tx["gas"]:
            tx["gas"] = gas_limit

        if self.get_balance() < self.w3.fromWei(tx["gas"], "ether"):
            raise Exception(f"not enough for gas fee {self.get_balance()}")

        build_tx = contract.constructor(
            cap=cap, name_=name, symbol_=symbol, minter=minter
        ).buildTransaction(tx)
        tx_receipt = self._transction(build_tx)
        contract_address = tx_receipt.contractAddress
        logger.info("deploy new erc20 contract: %s", contract_address)
        return contract_address

    def get_trx(self, tx_id_hex: str):
        receipt = self.w3.eth.getTransactionReceipt(tx_id_hex)
        return receipt

    async def check_trx(self, tx_id_hex, times=10):
        for i in range(times):
            try:
                receipt = self.w3.eth.getTransactionReceipt(tx_id_hex)
            except Exception as e:
                logger.error(e)
                receipt = None
            if receipt:
                if receipt["status"] == 1:
                    msg = "Transaction completed successfully"
                    status = True
                else:
                    msg = "Transaction failed"
                    status = False
            else:
                msg = "Transaction not found"
                status = False
            if status:
                break
            await asyncio.sleep(1)
        return msg, status


class RumERC20Instance:
    """
    https://github.com/rumsystem/rum-eth-mvm/blob/main/dapps/RumERC20/contracts/RumERC20.sol
    """
    def __init__(
        self, contract_address, pvtkey=None, chain: RumEthChain = None, abi=None
    ):
        abi = abi or RumERC20_abi
        self.chain = chain or RumEthChain(pvtkey)
        self.w3 = self.chain.w3
        self.account = self.chain.account
        self.erc20 = self.chain.w3.eth.contract(contract_address, abi=abi)
        self.funcs = self.erc20.functions

    def name(self):
        return self.funcs.name().call()

    def symbol(self):
        return self.funcs.symbol().call()

    def decimals(self):
        return self.funcs.decimals().call()

    def total_supply(self):
        unit256 = self.funcs.totalSupply().call()
        return self.w3.fromWei(unit256, "ether")

    def get_balance(self, address=None):
        address = address or self.account.address
        address = self.w3.toChecksumAddress(address)
        unit256 = self.funcs.balanceOf(address).call()
        return self.w3.fromWei(unit256, "ether")

    def get_rum_balance(self, address=None):
        address = address or self.account.address
        return self.chain.get_balance(address)

    def transfer(self, to_address, num):
        """transfter num of token to address"""
        to_address = self.w3.toChecksumAddress(to_address)
        amount = self.w3.toWei(num, "ether")

        options = {
            "gas": 53000,
            "gasPrice": self.w3.toWei("1", "gwei"),
            "from": self.account.address,
            "nonce": self.w3.eth.getTransactionCount(self.account.address),
        }
        gas_limit = self.w3.eth.estimateGas(options)
        if gas_limit > options["gas"]:
            options["gas"] = gas_limit

        tx = self.funcs.transfer(to_address, amount).buildTransaction(options)
        signed = self.w3.eth.account.signTransaction(
            tx, private_key=self.account.privateKey
        )
        tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction)
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        tid = tx_receipt.transactionHash.hex()
        logger.info("transfer to %s is done by trx: %s", to_address, tid)
        return tid

    def get_trx(self, tx_id_hex: str):
        return self.chain.get_trx(tx_id_hex)
