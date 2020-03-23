import sys
sys.path.append('../')

from swingby import NodeHttpClient

node = NodeHttpClient("https://testnet-node.swingby.network")
peers = node.get_peers()

for p in peers:
    print ("Moniker: {} Id: {}".format(p['moniker'], p['id']))
