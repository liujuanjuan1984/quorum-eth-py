import logging

from web3 import Web3

from quorum_eth_py._http import HttpRequest

logger = logging.getLogger(__name__)


GATEWAY_API_BASE = "https://prs-bp2.press.one/api"


class RumEthChainGateway:
    """
    the gateway of rum-eth chain with mixin network
    https://github.com/rumsystem/rum-eth-mvm/blob/main/PAYMENT-GATEWAY.md
    """

    def __init__(self, api_base: str = GATEWAY_API_BASE):
        self.http = HttpRequest(api_base)
        self.w3 = Web3()
