"""
This module contains classes for interacting with the Swingby network via REST
"""

import asyncio
import aiohttp
import time
import json

def default_send_get():
    pass

def default_send_post():
    pass

class NodeHttpClient:
    """
    BFX rest interface contains functions which are used to interact with both the public
    and private Bitfinex http api's.
    To use the private api you have to set the API_KEY and API_SECRET variables to your
    api key.
    """

    def __init__(self, url, sendGetRequestFunc=default_send_get, sendPostRequestFunc=default_send_post, loop=None *args, **kwargs):
        self.loop = loop or asyncio.get_event_loop()
        self.url = url
        self.get = sendGetRequestFunc
        self.post = sendPostRequestFunc

    def create_float(self):
        """
        Create a float deposit record
        https://testnet-node.swingby.network/docs#operation/createFloat

        # Returns
        @return dict float
        @return string float.amount
        @return string float.currency
        @return string float.hash
        @return string float.nonce
        """
        pass
    
    def query_floats(self):
        """
        Query all float records
        https://testnet-node.swingby.network/docs#operation/queryFloats

        # Attributes
        @param string hash - Hash of the inbound float
        @param string chain - Currency (BTC, BNB ...)
        @param string address - Swap inbound address
        @param string status - Status of swap (pending | active | expired)
        @param integer page_size - Max number of items per page
        @param integer page - Page number
        @param integer sort - if sort = 1 then results are old - new
        @param string OrInHash - Hash of the inbound transaction (OR match)
        @param string OrHash - Hash of the outbound transaction (OR match)
        @param string OrInAddress - Swap inbound address (OR match)
        """
        pass

    def get_tss_addresses(self):
        """
        Get the nodes TSS addresses
        https://testnet-node.swingby.network/docs#operation/getAddresses

        # Returns
        @return dict addresses
        @return string addresses[n].address
        @return string addresses[n].currency
        """
        pass

    def get_peers(self):
        """
        Get a list of peers connected to the node
        https://testnet-node.swingby.network/docs#operation/getPeers

        # Attributes
        @param string type - node type (signer | default: normal)

        # Returns
        @return array peers
        """
        pass

    def get_stakes(self):
        """
        Get all stakes on the network
        https://testnet-node.swingby.network/docs#operation/getStakes

        # Returns
        @return array stakes
        @return string stakes.address
        @return string stakes.amount
        @return string stakes.stakeTxHash
        @return integer stakes.stakeTime
        @return boolean stakes.stakeValid
        """
        pass

    def get_status(self):
        """
        Get node state and network metadata
        https://testnet-node.swingby.network/docs#operation/getStatus

        # Returns
        @return dict NodeStatus
        @return dict NodeStatus.nodeInfo
        @return dict NodeStatus.swapInfo
        """
        pass

    def calculate_swap(self):
        """
        Calculates the actual amount that the user will receive and fees for a given swap
        https://testnet-node.swingby.network/docs#operation/calculateSwap

        # Attributes
        @param string address_to - Payout address
        @param string amount - Amount of funds to swap
        @param string currency_from - Currency from (BTC, BNB, ...)
        @param string currency_to - Currency to (BTC, BNB ...)

        # Returns
        @return dict swap
        @return string swap.currency_from
        @return string swap.currency_to
        @return string swap.fee
        @return string swap.receive_amount
        @return string swap.send_amount
        @return integer swap.nonce
        """
        pass

    def create_swap(self):
        """
        Creates a swap record
        https://testnet-node.swingby.network/docs#operation/createSwap

        # Attributes
        @param string address_to - Payout address
        @param string amount - Amount of funds to swap
        @param currency_from - Currency from (BTC, BNB ...)
        @param currency_to - Currency to (BTC, BNB, ...)
        @param nonce - PoW nonce

        # Returns
        @return dict swap
        @return string swap.address_in
        @return string swap.address_out
        @return string swap.amount_in
        @return string swap.currency_in
        @return string swap.currency_out
        @return integer swap.timestamp
        """
        pass

    def swap(self):
        """
        Calculates PoW and creates a swap record

        # Attributes
        @param address_to - Payout address
        @param amount - Amount of funds to swap
        @param currency_from - Currency from (BTC, BNB ...)
        @param currency_to - Currency to (BTC, BNB ...)

        # Returns
        @return dict swap
        @return string swap.addressIn
        @return string swap.addressOut
        @return string swap.amountIn
        @return string swap.currencyIn
        @return string swap.currencyOut
        @return integer swap.timestamp
        @return dict swap.calc - response from calculate_swap
        """
        pass

    def get_swap_fees(self):
        """
        Get the fees for performing a swap
        https://testnet-node.swingby.network/docs#operation/getSwapFees

        # Returns
        @return array fees
        @return string fees[n].bridgeFeePercent
        @return string fees[n].currency
        @return string fees[n].minerFee
        """
        pass

    def query_swaps(self):
        """
        Query swaps
        https://testnet-node.swingby.network/docs#operation/queryTransactions

        # Attributes
        @param string in_hash
        @param string out_hash
        @param string to_chain
        @param string from_chain
        @param string in_address
        @param string out_address
        @param string status
        @param integer page_size
        @param integer page
        @param integer sort
        @param string OR_in_hash
        @param string OR_out_hash
        
        # Returns
        @return dict swaps
        @return integer swaps.itemCount
        @return integer swaps.total
        @return dict swaps.items
        """
        pass

    def get_swap_stats(self):
        """
        Get performance statistics 
        https://testnet-node.swingby.network/docs#operation/getSwapStats

        # Returns
        @return dict stats
        @return array stats.network1mSwaps
        @return array stats.network1mSwapsVolume
        @return array stats.network24hrSwaps
        @return array stats.network24hrSwapsVolume
        @return array stats.networkRewards1mVolume
        @return array stats.networkRewards24hrVolume
        @return number stats.networkRewardsVolume
        @return number stats.networkSwaps
        @return number stats.networkSwapsVolume
        @return array stats.participated1mSwaps
        @return array stats.participated1mSwapsVolume
        @return array stats.participated24hrSwaps
        @return array stats.participated24hrSwapsVolume
        @return number stats.participatedSwaps
        @return number stats.participatedSwapsVolume
        @return array stats.rewards1mVolume
        @return array stats.rewards24hrVolume
        @return number stats.rewardsVolume
        """
        pass