import sys
import json
sys.path.append('../')

from swingby import NodeHttpClient

node = NodeHttpClient("https://testnet-node.swingby.network")
swaps = node.query_swaps(in_address="tbnb1z20t7rn6urh46m2tavny3ap9n0pvkf47mynuza", status="COMPLETED")

for s in swaps['items']:
    print("{} {} -> {} {} | {}".format(s['amountIn'], s['addressIn'], s['amountOut'],
                                        s['addressOut'], s['status']))
