# betdaq-retail
Python wrapper for BETDAQ Retail API.

[Betdaq Documentation](http://api.betdaq.com/v2.0/Docs/default.aspx)

# Installation

```
$ pip install betdaq-retail
```

# Usage

```python
>>> from betdaq.apiclient import APIClient
>>> api = APIClient('username', 'password')
>>> sport_ids = api.marketdata.get_sports()
>>> all_markets = api.marketdata.get_sports_markets([100005]) 
```
