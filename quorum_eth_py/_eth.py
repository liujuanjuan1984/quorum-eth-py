import logging

from web3 import Web3
from web3.middleware import geth_poa_middleware

from quorum_eth_py._browser import RumEthChainBrowser
from quorum_eth_py.contract.RumERC20 import abi as RumERC20_abi
from quorum_eth_py.contract.RumERC20 import bytecode as RumERC20_bytecode

logger = logging.getLogger(__name__)


RUM_ETH_HTTP_PROVIDER = "http://149.56.22.113:8545"
RUM_ETH_CHAINID = 19890609


class RumEthChain:
    def __init__(self, pvtkey, provider=None):
        provider = provider or RUM_ETH_HTTP_PROVIDER
        self.w3 = Web3(Web3.HTTPProvider(provider))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        logger.info("connected to rum-eth chain status: %s", self.w3.isConnected())
        self.account = self.w3.eth.account.from_key(pvtkey)
        self.w3.eth.defaultAccount = self.account.address
        logger.info("account address: %s", self.account.address)

    def get_balance(self, address=None):
        """get the balance of address, default is the account address"""
        address = address or self.account.address
        address = self.w3.toChecksumAddress(address)
        balance_wei = self.w3.eth.getBalance(address)
        balance = self.w3.fromWei(balance_wei, "ether")
        return balance

    def transfer(self, to_address, num):
        """transfer rum to address, the rum is origin token of poa chain, used as gas feed"""
        # check balance of account
        if self.get_balance() < num:
            raise Exception("balance not enough")

        tx = {
            "nonce": self.w3.eth.getTransactionCount(self.account.address),
            "to": self.w3.toChecksumAddress(to_address),
            "value": self.w3.toWei(num, "ether"),
            "gasPrice": self.w3.toWei("10", "gwei"),
            "gas": 21000,
            "chainId": RUM_ETH_CHAINID,
        }

        signed_tx = self.w3.eth.account.sign_transaction(
            tx, private_key=self.account.privateKey
        )
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)

        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        tid = tx_receipt.transactionHash.hex()
        logger.info("Transaction confirmed: %s", tid)
        return tid

    def contract(self, abi, contract_address):
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
        gas_limit = contract.constructor(
            cap=cap, name_=name, symbol_=symbol, minter=minter
        ).estimateGas()
        tx = {
            "from": self.account.address,
            "nonce": self.w3.eth.getTransactionCount(self.account.address),
            "gasPrice": self.w3.toWei("10", "gwei"),
            "gas": gas_limit,
            "chainId": RUM_ETH_CHAINID,
        }
        build_tx = contract.constructor(
            cap=cap, name_=name, symbol_=symbol, minter=minter
        ).buildTransaction(tx)
        signed_tx = self.w3.eth.account.sign_transaction(
            build_tx, private_key=self.account.privateKey
        )
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        contract_address = tx_receipt.contractAddress
        logger.info("deploy new erc20 contract: %s", contract_address)
        erc20 = RumERC20Instance(contract_address, chain=self, abi=abi)
        return erc20


class RumERC20Instance:
    def __init__(
        self, contract_address, pvtkey=None, chain: RumEthChain = None, abi=None
    ):
        abi = abi or RumERC20_abi
        if chain is None and pvtkey is None:
            raise Exception("chain or pvtkey must be provided")
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

    def transfer(self, to_address, num):
        """transfter num of token to address"""
        to_address = self.w3.toChecksumAddress(to_address)
        amount = self.w3.toWei(num, "ether")

        options = {
            "gas": 210000,
            "gasPrice": self.w3.toWei("1", "gwei"),
            "from": self.account.address,
            "nonce": self.w3.eth.getTransactionCount(self.account.address),
        }
        tx = self.funcs.transfer(to_address, amount).buildTransaction(options)
        signed = self.w3.eth.account.signTransaction(
            tx, private_key=self.account.privateKey
        )
        tx_id = self.w3.eth.sendRawTransaction(signed.rawTransaction)
        tx_id_hex = tx_id.hex()
        logger.info("transfer to %s is done by trx: %s", to_address, tx_id_hex)
        return tx_id_hex
