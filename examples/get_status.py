import sys
sys.path.append('../')

from swingby import NodeHttpClient

node = NodeHttpClient("https://testnet-node.swingby.network")
status = node.get_status()

print ("Node status:")
print ("Moniker:", status['nodeInfo']['moniker'])
print ("Addr:", status['nodeInfo']['listenAddr'])
print ("CollateralStaked:", status['swapInfo']['stakeAmount'])
