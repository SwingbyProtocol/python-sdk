import sys
sys.path.append('../')

from swingby import NodeHttpClient

node = NodeHttpClient("https://testnet-node.swingby.network")
addresses = node.get_tss_addresses()

for a in addresses:
    print ("{}: {}".format(a['currency'], a['address']))
