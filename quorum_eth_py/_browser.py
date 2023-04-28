import logging

from web3 import Web3

from quorum_eth_py._http import HttpRequest

logger = logging.getLogger(__name__)


BROWSER_API_BASE = "http://explorer.rumsystem.net/api"


class RumEthChainBrowser:
    """the browser of rum-eth chain"""

    def __init__(self, contract_address=None, api_base: str = BROWSER_API_BASE):
        self.contract_address = contract_address
        self.http = HttpRequest(api_base)
        self.api_base = api_base or BROWSER_API_BASE
        self.w3 = Web3()

    def _get_contract(self, action, contract_address=None):
        contract_address = contract_address or self.contract_address
        data = self.http.get(
            f"?module=token&action={action}&contractaddress={contract_address}"
        )
        if data.get("status") != "1":
            logger.warning("get_contract error: %s", data)
            return {}
        return data.get("result", {})

    def get_contract_info(self, contract_address=None):
        return self._get_contract("getToken", contract_address)

    def get_contract_holders(self, contract_address=None):
        return self._get_contract("getTokenHolders", contract_address)

    def contract_holders(self, contract_address=None):
        data = self.get_contract_holders(contract_address)
        holders = {
            self.w3.toChecksumAddress(i.get("address")): i.get("value", 0) for i in data
        }
        return holders

    def is_minted(self, to_address, contract_address=None):
        holders = self.contract_holders(contract_address)
        try:
            minted = self.w3.toChecksumAddress(to_address) in holders
        except ValueError as err:
            minted = to_address in holders
            logger.warning("%s is_minted error: %s", to_address, err)
        return minted
