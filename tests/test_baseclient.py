import unittest
from zeep import Client

from betdaq.baseclient import BaseClient


class BaseClientTest(unittest.TestCase):

    def test_baseclient_init(self):
        client = BaseClient(
            username="username",
            password="password",
            wsdl_file="tests/resources/API.wsdl",
        )
        assert client.username == "username"
        assert client.password == "password"
        assert client.wsdl_file == "tests/resources/API.wsdl"
        assert client.external_headers == {
            "version": 2.0,
            "languageCode": "en",
            "username": "username",
            "password": "password",
            "applicationIdentifier": None,
        }

        assert isinstance(client.secure_client, Client)
        assert isinstance(client.readonly_client, Client)
