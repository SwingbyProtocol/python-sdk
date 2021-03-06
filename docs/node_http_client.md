
# swingby

This module contains various clients for interacting with the Swingby network


# NodeHttpClient
```python
NodeHttpClient(
    self,
    url,
    sendGetRequestFunc=<function default_send_get at 0x7f44d64d4e60>,
    sendPostRequestFunc=<function default_send_post at 0x7f44d5b36ef0>,
    *args,
    **kwargs)
```

NodeHttpClient includes functions for interacting with the Swingby network. For use simply initiate an instance of the NodeHttpClient
With a url pointing to either your node or a Swingby hosted node. Example:

node = NodeHttpClient("https://testnet-node.swingby.network")


## create_float
```python
NodeHttpClient.create_float()
```

Create a float deposit record
https://testnet-node.swingby.network/docs#operation/createFloat

__Returns__

@return dict float
@return string float.amount
@return string float.currency
@return string float.hash
@return string float.nonce


## query_floats
```python
NodeHttpClient.query_floats()
```

Query all float records
https://testnet-node.swingby.network/docs#operation/queryFloats

__Attributes__

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


## get_tss_addresses
```python
NodeHttpClient.get_tss_addresses()
```

Get the nodes TSS addresses
https://testnet-node.swingby.network/docs#operation/getAddresses

__Returns__

@return dict addresses
@return string addresses[n].address
@return string addresses[n].currency


## get_peers
```python
NodeHttpClient.get_peers(node_type='normal')
```

Get a list of peers connected to the node
https://testnet-node.swingby.network/docs#operation/getPeers

__Attributes__

- `@param string type - node type (signer | default`: normal)

__Returns__

@return array peers


## get_stakes
```python
NodeHttpClient.get_stakes()
```

Get all stakes on the network
https://testnet-node.swingby.network/docs#operation/getStakes

__Returns__

@return array stakes
@return string stakes.address
@return string stakes.amount
@return string stakes.stakeTxHash
@return integer stakes.stakeTime
@return boolean stakes.stakeValid


## get_status
```python
NodeHttpClient.get_status()
```

Get node state and network metadata
https://testnet-node.swingby.network/docs#operation/getStatus

__Returns__

@return dict NodeStatus
@return dict NodeStatus.nodeInfo
@return dict NodeStatus.swapInfo


## calculate_swap
```python
NodeHttpClient.calculate_swap(address_to, amount, currency_from,
                              currency_to, **kwargs)
```

Calculates the actual amount that the user will receive and fees for a given swap
https://testnet-node.swingby.network/docs#operation/calculateSwap

__Attributes__

@param string address_to - Payout address
@param string amount - Amount of funds to swap
@param string currency_from - Currency from (BTC, BNB, ...)
@param string currency_to - Currency to (BTC, BNB ...)

__Returns__

@return dict swap
@return string swap.currency_from
@return string swap.currency_to
@return string swap.fee
@return string swap.receive_amount
@return string swap.send_amount
@return integer swap.nonce


## create_swap
```python
NodeHttpClient.create_swap(address_to, amount, currency_from,
                           currency_to, nonce, **kwargs)
```

Creates a swap record
https://testnet-node.swingby.network/docs#operation/createSwap

__Attributes__

@param string address_to - Payout address
@param string amount - Amount of funds to swap
@param currency_from - Currency from (BTC, BNB ...)
@param currency_to - Currency to (BTC, BNB, ...)
@param nonce - PoW nonce

__Returns__

@return dict swap
@return string swap.address_in
@return string swap.address_out
@return string swap.amount_in
@return string swap.currency_in
@return string swap.currency_out
@return integer swap.timestamp


## swap
```python
NodeHttpClient.swap(address_to, amount, currency_from, currency_to,
                    **kwargs)
```

Calculates PoW and creates a swap record

__Attributes__

@param address_to - Payout address
@param amount - Amount of funds to swap
@param currency_from - Currency from (BTC, BNB ...)
@param currency_to - Currency to (BTC, BNB ...)

__Returns__

@return dict swap
@return string swap.addressIn
@return string swap.addressOut
@return string swap.amountIn
@return string swap.currencyIn
@return string swap.currencyOut
@return integer swap.timestamp
@return dict swap.calc - response from calculate_swap


## get_swap_fees
```python
NodeHttpClient.get_swap_fees()
```

Get the fees for performing a swap
https://testnet-node.swingby.network/docs#operation/getSwapFees

__Returns__

@return array fees
@return string fees[n].bridgeFeePercent
@return string fees[n].currency
@return string fees[n].minerFee


## query_swaps
```python
NodeHttpClient.query_swaps(in_hash=None,
                           out_hash=None,
                           to_chain=None,
                           from_chain=None,
                           in_address=None,
                           out_address=None,
                           status=None,
                           page_size=None,
                           page=None,
                           sort=None,
                           OR_in_hash=None,
                           OR_out_hash=None,
                           **kwargs)
```

Query swaps
https://testnet-node.swingby.network/docs#operation/queryTransactions

__Attributes__

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

__Returns__

@return dict swaps
@return integer swaps.itemCount
@return integer swaps.total
@return dict swaps.items


## get_swap_stats
```python
NodeHttpClient.get_swap_stats()
```

Get performance statistics
https://testnet-node.swingby.network/docs#operation/getSwapStats

__Returns__

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

