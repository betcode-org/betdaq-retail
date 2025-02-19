import unittest


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from betdaq import baseclient

        baseclient.WSDL_FILE = "resources/API.wsdl"
