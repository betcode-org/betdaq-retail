from tests import BaseTestCase
from betdaq.apiclient import APIClient
from betdaq.endpoints import Betting, Account, MarketData, Trading


class APIClientTest(BaseTestCase):

    def test_apiclient_init(self):
        client = APIClient("username", "password")
        assert str(client) == "APIClient"
        assert repr(client) == "<APIClient [username]>"
        assert isinstance(client.betting, Betting)
        assert isinstance(client.account, Account)
        assert isinstance(client.marketdata, MarketData)
        assert isinstance(client.trading, Trading)
