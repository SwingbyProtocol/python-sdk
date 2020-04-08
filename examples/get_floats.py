import sys
sys.path.append('../')

from swingby import StakesHttpClient

api = StakesHttpClient("https://staking-api.swingby.network")
floats = api.get_floats()

print (floats['BTC'])
print (floats['BNB'])
