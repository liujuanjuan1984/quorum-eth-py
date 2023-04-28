import logging

from quorum_eth_py import RumEthChainBrowser

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

bot = RumEthChainBrowser("0x2317B756bA89E87A7AACf63007b2e57A6a60D57a")

"""
_info = {
    "cataloged": True,
    "contractAddress": "0x2317b756ba89e87a7aacf63007b2e57a6a60d57a",
    "decimals": "",
    "name": "Rum Dev Club",
    "symbol": "DEV",
    "totalSupply": "18",
    "type": "ERC-721",
}
"""
info = bot.get_contract_info()
print(info)

"""
_holders_list = [
    {"address": "0x9966e95017616bb4ca4e05d9afb15faa841adf37", "value": "4"},
    {"address": "0xf60d8d37665d52c4766127739fc7d20f6c833af7", "value": "1"},
    {"address": "0x91b8343cfb1a75a9b2ecb69d49d60c86c97d55b5", "value": "1"},
    {"address": "0x689f98dbfec21d9a1229b4d08db66a694fafb166", "value": "1"},
    {"address": "0x650e2b6eee09a85c99c4b575115239b5094ee505", "value": "1"},
    {"address": "0x65060a343c0195e11df8273822b61e525cab4138", "value": "1"},
    {"address": "0x552cdbaeee82daaa8c331113ab718560c4c5e39d", "value": "1"},
    {"address": "0x49aa4068af67fb35fed94742f9ff6ed58121ab37", "value": "1"},
    {"address": "0x393c01ce59dd861782a52310b3a1aa701df695b0", "value": "1"},
    {"address": "0x2e03400b742fef77e7968d3345c023530da40dfd", "value": "1"},
]
"""
holders = bot.get_contract_holders()
print(holders)

"""
_holders_dict = {
    "0x9966E95017616bB4Ca4e05D9aFB15fAA841ADF37": "4",
    "0xf60d8D37665D52C4766127739FC7D20F6c833aF7": "1",
    "0x91b8343CFb1A75a9B2Ecb69D49d60c86C97D55b5": "1",
    "0x689F98DBFec21d9a1229B4D08Db66a694Fafb166": "1",
    "0x650E2B6eee09a85C99c4b575115239b5094ee505": "1",
    "0x65060a343C0195E11df8273822b61E525Cab4138": "1",
    "0x552CdbaeEE82Daaa8C331113aB718560C4c5e39d": "1",
    "0x49aa4068AF67fB35fed94742f9fF6ed58121ab37": "1",
    "0x393c01CE59dd861782A52310b3a1AA701Df695b0": "1",
    "0x2E03400b742FeF77e7968d3345C023530dA40Dfd": "1",
}
"""
holders = bot.contract_holders()
print(holders)

print(bot.is_minted("0x2E03400b742FeF77e7968d3345C023530dA40Dfd") == True)
print(bot.is_minted("0x2E03400b7x2FeF77e7968d3345C023530dA40Dfd") == False)
