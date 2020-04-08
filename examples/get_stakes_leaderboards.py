import sys
sys.path.append('../')

from swingby import StakesHttpClient

api = StakesHttpClient("https://staking-api.swingby.network")
leaderboard = api.get_leaderboard()

for l in leaderboard['items']:
    print ("Address {} has staked {} SWINGBY".format(l["address"], l["stake"]))
