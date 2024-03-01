#!/usr/bin/python3

"""
              BiPy
---------------------------------
Binance Wrapper API gateway tests
---------------------------------

"""

from gateway import create_gateway
import unittest
import logging


class TestAPIGateway(unittest.TestCase):
    """
    Implementation of tests for our Binance API wrapper gateway
    """
    def setUp(self):
        # Instantiating the gateway
        self.app = create_gateway(public=True)

        # Creating an app client dedicated to the testing of the gateway
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_get_tickers(self):
        """
        Testing the get_tickers gateway method
        """
        try:
            response = self.client.get('/get_tickers')
        except Exception as e:
            logging.error(f"An error occurred when testing the get_tickers endpoint : {e}")
            raise e

        # Testing the response status code
        self.assertEqual(first=response.status_code,
                         second=200,
                         msg='Invalid response')

    def test_get_ticker_data(self):
        """
        Testing the get_ticker_data gateway method
        """
        try:
            response = self.client.get('/get_ticker_data/BTCUSDT/2023-12-31/2024-01-01/1h')
        except Exception as e:
            logging.error(f"An error occurred when testing the get_ticker_data endpoint : {e}")
            raise e

        self.assertEqual(response.status_code, 200)

    def test_get_data(self):
        """
        Testing the get_ticker_data gateway method
        """
        try:
            response = self.client.get('/get_data/["BTCUSDT", "ETHUSDT"]/2023-12-31/2024-01-01/1h')
        except Exception as e:
            logging.error(f"An error occurred when testing the get_ticker_data endpoint : {e}")
            raise e

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    # Running gateway tests
    unittest.main()
