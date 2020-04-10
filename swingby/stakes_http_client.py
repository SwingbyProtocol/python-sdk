"""
This module contains classes for interacting with the Swingby pre staking API
Which helps to deliver useful insights on the pre-staking system.
"""

import time
import json
from .utils import default_send_get, default_send_post

class StakesHttpClient:
    """
    NodeHttpClient includes functions for interacting with the Swingby network. For use simply initiate an instance of the NodeHttpClient
    With a url pointing to either your node or a Swingby hosted node. Example:

    node = StakesHttpClient("https://staking-api.swingby.network")
    """

    def __init__(self, url, sendGetRequestFunc=default_send_get, sendPostRequestFunc=default_send_post, *args, **kwargs):
        if not url:
            url = "https://staking-api.swingby.network"
        self.url = url
        self.get = sendGetRequestFunc
        self.post = sendPostRequestFunc

    def _url(self, path):
        return "{}/{}".format(self.url, path)

    def get_leaderboard(self, memo=None, page=1, page_size=25):
        """
        Get the staking leaderboards

        # Attributes
        @param string memo - Weekly memo (none provided = current_memo)
        @param integer page - Page number
        @param integer page_size - Number of items per page

        # Returns
        @return dict leaderboard
        @return array leaderboard.items
        @return integer leaderboard.itemCount
        @return integer leaderboard.total
        @return float leaderboard.totalStaked
        """
        query = {
            "page": page,
            "page_size": page_size
        }
        if memo:
            query["memo"] = memo
        return self.get(self._url("v1/stakes/leaderboard"), query=query)

    def get_floats(self):
        """
        Get network floats

        # Returns
        @return object balances
        @return object balances.BTC
        @return object balances.BNB
        """
        res = self.get(self._url("v1/floats"))
        return res['balances']

    def get_platform_status(self):
        """
        Gets the status of the platform (0 = offline, 1 = online, 3 = maintenance)

        # Returns
        @return integer status
        """
        res = self.get(self._url("v1/platform_status"))
        return res['status']

    def get_rewards_leaderboard(self, memo=None, page=1, page_size=25):
        """
        Gets the staking rewards leaderboard

        # Attributes
        @param string memo - Weekly memo (none provided = current_memo)
        @param integer page - Page number
        @param integer page_size - Number of items per page

        # Returns
        @return dict leaderboard
        @return array leaderboard.items
        @return integer leaderboard.itemCount
        @return integer leaderboard.total
        """
        query = {
            "page": page,
            "page_size": page_size
        }
        if memo:
            query["memo"] = memo
        return self.get(self._url("v1/stakes/rewards_leaderboard"), query=query)

    def get_holders(self, memo=None):
        """
        Gets the holders on the network - All addresses that own Swingby tokens

        # Attributes
        @param string memo - Weekly memo (none provided = current_memo)

        # Returns
        @return object holders
        @return float holders[address].quantity
        @return float holders[address].percentage
        """
        query = {}
        if not memo:
            query['memo'] = memo
        return self.get(self._url("v1/stakes/holders"), query=query)

    def get_payout(self, memo=None):
        """
        Generate the staking rewards payout transaction (un-signed)

        # Attributes
        @param string memo - Weekly memo (none provided = current_memo)

        # Returns
        @return object payout
        @return integer payout.totalTransactions
        @return string payout.estimatedPayout
        @return array payout.holders
        """
        query = {}
        if not memo:
            query['memo'] = memo
        return self.get(self._url("v1/stakes/holders"), query=query)

    def get_rewards_history(self, address):
        """
        Get all rewards for the given address

        # Returns
        @return object payout
        @return integer payout.totalTransactions
        @return string payout.estimatedPayout
        @return array payout.holders
        """
        query = {
            "address": address
        }
        return self.get(self._url("v1/stakes/rewards_history"), query=query)

    def get_weekly_memo(self):
        """
        Get the weekly memo

        # Returns
        @return string memo
        """
        return self.get(self._url("v1/stakes/weekly_memo"), json=False)

    def get_stakes(self, address=None, memo=None):
        """
        Get the network stakes

        # Returns
        @return array stakes
        @return string stakes[n].address
        @return string stakes[n].staked_amount
        @return string stakes[n].reward_amount
        @return string stakes[n].weekly_memo
        """
        query = {}
        if address:
            query['address'] = address
        if memo:
            query['memo'] = memo
        return self.get(self._url("v1/stakes"), query=query)

    def get_token_info(self):
        """
        Get token info

        # Returns
        @return object info
        """
        return self.get(self._url("v1/chain/asset"))

    def get_token_balance(self, address):
        """
        Get token balance

        # Returns
        @return object info
        """
        query = {
            "address": address
        }
        return self.get(self._url("v1/chain/asset"), query=query)
