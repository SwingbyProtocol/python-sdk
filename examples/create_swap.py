import sys
sys.path.append('../')

from swingby import NodeHttpClient

node = NodeHttpClient("https://testnet-node.swingby.network")
addr_to = "tbnb1dedxffvl324ggfdpxl0gw5hwylc848ztuy7g7c"
sr = node.swap(address_to=addr_to, amount="1.1", currency_from="BTC", currency_to="BTC.B")

print ("Swap:")
print ("Send {} ({}) to {}".format(sr['amountIn'], sr['currencyIn'], sr['addressIn']))
print ("Receive {} ({}) to {}".format(sr['calc']['receive_amount'], sr['currencyOut'], sr['addressOut']))
