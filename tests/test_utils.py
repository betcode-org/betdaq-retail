import unittest

from betdaq import utils, exceptions


class UtilsTest(unittest.TestCase):
    def test_check_status_code_valid(self):
        response = {"ReturnStatus": {"Code": 0}}
        self.assertIsNone(utils.check_status_code(response))

    def test_check_status_code_error(self):
        response = {"ReturnStatus": {"Code": 1}}
        self.assertRaises(exceptions.ResourceError, utils.check_status_code, response)

        response = {"ReturnStatus": {"Code": 11}}
        self.assertRaises(
            exceptions.SelectionDoesNotExist, utils.check_status_code, response
        )

        response = {"ReturnStatus": {"Code": 19}}
        self.assertRaises(
            exceptions.InsufficientVirtualPunterFunds, utils.check_status_code, response
        )

    def test_check_status_code_map_missing(self):
        response = {"ReturnStatus": {"Code": 12345}}
        self.assertRaises(
            exceptions.UnknownStatusCode, utils.check_status_code, response
        )
