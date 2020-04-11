
# swingby

This module contains various clients for interacting with the Swingby network


# StakesHttpClient
```python
StakesHttpClient(
    self,
    url,
    sendGetRequestFunc=<function default_send_get at 0x7f8f881f8cb0>,
    sendPostRequestFunc=<function default_send_post at 0x7f8f88206170>,
    *args,
    **kwargs)
```

NodeHttpClient includes functions for interacting with the Swingby network. For use simply initiate an instance of the NodeHttpClient
With a url pointing to either your node or a Swingby hosted node. Example:

node = StakesHttpClient("https://staking-api.swingby.network")


## get_leaderboard
```python
StakesHttpClient.get_leaderboard(memo=None, page=1, page_size=25)
```

Get the staking leaderboards

__Attributes__

@param string memo - Weekly memo (none provided = current_memo)
@param integer page - Page number
@param integer page_size - Number of items per page

__Returns__

@return dict leaderboard
@return array leaderboard.items
@return integer leaderboard.itemCount
@return integer leaderboard.total
@return float leaderboard.totalStaked


## get_floats
```python
StakesHttpClient.get_floats()
```

Get network floats

__Returns__

@return object balances
@return object balances.BTC
@return object balances.BNB


## get_platform_status
```python
StakesHttpClient.get_platform_status()
```

Gets the status of the platform (0 = offline, 1 = online, 3 = maintenance)

__Returns__

@return integer status


## get_rewards_leaderboard
```python
StakesHttpClient.get_rewards_leaderboard(memo=None,
                                         page=1,
                                         page_size=25)
```

Gets the staking rewards leaderboard

__Attributes__

@param string memo - Weekly memo (none provided = current_memo)
@param integer page - Page number
@param integer page_size - Number of items per page

__Returns__

@return dict leaderboard
@return array leaderboard.items
@return integer leaderboard.itemCount
@return integer leaderboard.total


## get_holders
```python
StakesHttpClient.get_holders(memo=None)
```

Gets the holders on the network - All addresses that own Swingby tokens

__Attributes__

@param string memo - Weekly memo (none provided = current_memo)

__Returns__

@return object holders
@return float holders[address].quantity
@return float holders[address].percentage


## get_payout
```python
StakesHttpClient.get_payout(memo=None)
```

Generate the staking rewards payout transaction (un-signed)

__Attributes__

@param string memo - Weekly memo (none provided = current_memo)

__Returns__

@return object payout
@return integer payout.totalTransactions
@return string payout.estimatedPayout
@return array payout.holders


## get_rewards_history
```python
StakesHttpClient.get_rewards_history(address)
```

Get all rewards for the given address

__Returns__

@return object payout
@return integer payout.totalTransactions
@return string payout.estimatedPayout
@return array payout.holders


## get_weekly_memo
```python
StakesHttpClient.get_weekly_memo()
```

Get the weekly memo

__Returns__

@return string memo


## get_stakes
```python
StakesHttpClient.get_stakes(address=None, memo=None)
```

Get the network stakes

__Returns__

@return array stakes
@return string stakes[n].address
@return string stakes[n].staked_amount
@return string stakes[n].reward_amount
@return string stakes[n].weekly_memo


## get_token_info
```python
StakesHttpClient.get_token_info()
```

Get token info

__Returns__

@return object info


## get_token_balance
```python
StakesHttpClient.get_token_balance(address)
```

Get token balance

__Returns__

@return object info

