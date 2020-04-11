# Swingby SDK for Python

An implementation of the Swingby standard development kit for Python3.

## Features:

* Official implementation
* Http Client
* Tustless swaps between ECDSA chains

## Instillation

```bash
git clone https://github.com/SwingbyProtocol/python-sdk.git"
pip install ./python-sdk
```

## Quickstart

Initiate a HTTP connection to one of our testnet nodes:

```python
from swingby import NodeHttpClient
node = NodeHttpClient("https://testnet-node.swingby.network")
```

Create a trustless swap deposit

```python
node = NodeHttpClient("https://testnet-node.swingby.network")
addr_to = "tbnb1dedxffvl324ggfdpxl0gw5hwylc848ztuy7g7c"
sr = node.swap(address_to=addr_to, amount="1.1", currency_from="BTC", currency_to="BTC.B")
```

Query last 5 completed swaps

```python
node = NodeHttpClient("https://testnet-node.swingby.network")
swaps = node.query_swaps(page_size=5, status="COMPLETED")
```

for more examples on how to retrieve data from a node and interact with the Swingby network, please head to the [examples `examples/`](/examples) folder.

## Docs

* Documentation for our NodeSdk [here `docs/node_http_client.md`](/docs/node_http_client.md)
* Documentation for our StakesApiSdk [here `docs/stakes_http_client.md`](/docs/stakes_http_client.md)

For documentation on our node API, please visit [testnet-node.swingby.network/docs](https://testnet-node.swingby.network/).

## Useful links

* [Website](https://swingby.network)
* [Swingby explorer](https://bridge-testnet.swingby.network/explorer)
* [Swingby network dashboard](https://testnet-node.swingby.network/)

