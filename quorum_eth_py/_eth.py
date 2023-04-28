import logging

from web3 import Web3
from web3.middleware import geth_poa_middleware

from quorum_eth_py._browser import RumEthChainBrowser

logger = logging.getLogger(__name__)


RUM_ETH_HTTP_PROVIDER = "http://149.56.22.113:8545"


class RumEthChain:
    def __init__(self, provider=None):
        provider = provider or RUM_ETH_HTTP_PROVIDER
        self.w3 = Web3(Web3.HTTPProvider(provider))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        logger.info("connected to rum-eth chain status: %s", self.w3.isConnected())


class RumEthChainContract(RumEthChain):
    def __init__(self, abi, contract_address, owner_pvtkey):
        super().__init__()
        self.browser = RumEthChainBrowser(contract_address)
        self.owner = self.w3.eth.account.from_key(owner_pvtkey)
        self.w3.eth.default_account = self.owner.address
        self.contract_instance = self.w3.eth.contract(contract_address, abi=abi)
        contract_name = self.contract_instance.functions.name().call()
        logger.info("contract %s: %s", contract_name, contract_address)

    def mint_nft(self, to_address: str, unique_mint=True, minter_pvtkey=None):
        """mint nft to address"""
        to_address = self.w3.toChecksumAddress(to_address)
        if unique_mint:
            minted = self.browser.is_minted(to_address)
            logger.info(
                "%s minted: %s of %s ",
                to_address,
                minted,
                self.contract_instance.address,
            )
            if minted:
                logger.info("%s already minted", to_address)
                return True
        minter = self.owner
        if minter_pvtkey:
            minter = self.w3.eth.account.from_key(minter_pvtkey)
        options = {
            "gas": 1000000,
            "gasPrice": self.w3.toWei("1", "gwei"),
            "from": minter.address,
            "nonce": self.w3.eth.getTransactionCount(minter.address),
        }
        tx = self.contract_instance.functions.mint(to_address).buildTransaction(options)
        signed = minter.signTransaction(tx)
        tx_id = self.w3.eth.sendRawTransaction(signed.rawTransaction)
        tx_id_hex = tx_id.hex()
        logger.info("mint to %s is done by trx: %s", to_address, tx_id_hex)
        return tx_id_hex

    def get_balance(self, address: str):
        """get balance of address"""
        address = self.w3.toChecksumAddress(address)
        balance = self.contract_instance.functions.balanceOf(address).call()
        print("balance: ", balance)
        return balance

    def get_total_supply(self):
        """get total supply"""
        return self.contract_instance.functions.totalSupply().call()
