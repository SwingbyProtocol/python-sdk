"""
This module contains classes for interacting with the Swingby network via REST
"""

import time
import json

from .utils import default_send_get, default_send_post

class NodeHttpClient:
    """
    NodeHttpClient includes functions for interacting with the Swingby network. For use simply initiate an instance of the NodeHttpClient
    With a url pointing to either your node or a Swingby hosted node. Example:

    node = NodeHttpClient("https://testnet-node.swingby.network")
    """

    def __init__(self, url, sendGetRequestFunc=default_send_get, sendPostRequestFunc=default_send_post, *args, **kwargs):
        self.url = url
        self.get = sendGetRequestFunc
        self.post = sendPostRequestFunc

    def _url(self, path):
        return "{}/{}".format(self.url, path)

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
        raise Exception("create_float function not implemented.")

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
        raise Exception("query_floats function not implemented.")

    def get_tss_addresses(self):
        """
        Get the nodes TSS addresses
        https://testnet-node.swingby.network/docs#operation/getAddresses

        # Returns
        @return dict addresses
        @return string addresses[n].address
        @return string addresses[n].currency
        """
        return self.get(self._url("api/v1/addresses"))

    def get_peers(self, node_type="normal"):
        """
        Get a list of peers connected to the node
        https://testnet-node.swingby.network/docs#operation/getPeers

        # Attributes
        @param string type - node type (signer | default: normal)

        # Returns
        @return array peers
        """
        return self.get(self._url("api/v1/peers"), query={ "type": node_type })

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
        return self.get(self._url("api/v1/stakes"))

    def get_status(self):
        """
        Get node state and network metadata
        https://testnet-node.swingby.network/docs#operation/getStatus

        # Returns
        @return dict NodeStatus
        @return dict NodeStatus.nodeInfo
        @return dict NodeStatus.swapInfo
        """
        return self.get(self._url("api/v1/status"))

    def calculate_swap(self, address_to, amount, currency_from, currency_to, **kwargs):
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
        body = {
            "address_to": address_to,
            "amount": amount,
            "currency_from": currency_from,
            "currency_to": currency_to,
            **kwargs
        }
        return self.post(self._url("api/v1/swaps/calculate"), query={}, body=body)

    def create_swap(self, address_to, amount, currency_from, currency_to, nonce, **kwargs):
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
        body = {
            "address_to": address_to,
            "amount": amount,
            "currency_from": currency_from,
            "currency_to": currency_to,
            "nonce": nonce,
            **kwargs
        }
        return self.post(self._url("api/v1/swaps/create"), query={}, body=body)

    def swap(self, address_to, amount, currency_from, currency_to, **kwargs):
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
        calc = self.calculate_swap(address_to, amount, currency_from, currency_to, **kwargs)
        swap = self.create_swap(address_to, calc['send_amount'], currency_from, currency_to, calc['nonce'], **kwargs)
        return { **swap, "calc": calc }

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
        return self.get(self._url("api/v1/swaps/fees"))

    def query_swaps(self, in_hash=None, out_hash=None, to_chain=None, from_chain=None, in_address=None,
        out_address=None, status=None, page_size=None, page=None, sort=None, OR_in_hash=None,
        OR_out_hash=None, **kwargs):
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
        params = { **kwargs }
        if in_hash:
            params["in_hash"] = in_hash
        if out_hash:
            params["out_hash"] = out_hash
        if to_chain:
            params["to_chain"] = to_chain
        if from_chain:
            params["from_chain"] = from_chain
        if in_address:
            params["in_address"] = in_address
        if out_address:
            params["out_address"] = out_address
        if status:
            params["status"] = status
        if page_size:
            params["page_size"] = page_size
        if page:
            params["page"] = page
        if sort:
            params["sort"] = sort
        if OR_in_hash:
            params["OR_in_hash"] = OR_in_hash
        if OR_out_hash:
            params["OR_out_hash"] = OR_out_hash
        return self.get(self._url("api/v1/swaps/query"), query=params)

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
        return self.get(self._url("api/v1/swaps/stats"))

    def get_kv_store(self):
        """
        Get the nodes kv store. Only availbale if the node is in testnet mode
        https://testnet-node.swingby.network/docs#operation/getKVStore

        # Returns
        @return dict kvstore
        """
        kv_store = self.get(self._url("/api/v1/debug/kvstore"))
        return json.loads(kv_store)
