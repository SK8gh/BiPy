#!/usr/bin/python3

"""
            BiPy
----------------------------
Binance Wrapper testing file
----------------------------

"""

from winance import BinanceWrapper
from tests_configuration import *
import pandas as pd
import unittest
import logging


class TestBinanceWrapper(unittest.TestCase):
    """
    Testing of the Binance Wrapper class
    """
    @classmethod
    def setUpClass(cls):
        """
        Initializing the Binance Wrapper object once for all test methods
        """
        cls.bw = BinanceWrapper(api_key=None,
                                secret_key=None)

    def test_get_tickers(self):
        """
        Testing the 'BinanceWrapper.get_tickers' method
        -----------------------------------------------

        1. Testing that the symbols request passes through

        2. Function yields the right types:
            - returned object: list
            - elements in the returned list: str

        """
        try:
            symbols = self.bw.get_symbols()
        except Exception as e:
            logging.error('An error happened in the get_tickers method')
            raise e

        # Checking that the returned type(s) are adequate
        self.assertTrue(all(isinstance(s, str) for s in symbols))
        self.assertTrue(isinstance(symbols, list))

        # Checking that a few expected tickers are in the returned symbols
        for s in EXPECTED_SYMBOLS:
            self.assertIn(s, symbols, msg=f"Expecting {s} in the symbols")

    def test_get_ticker_data(self):
        """
        Testing the 'BinanceWrapper.get_data' method
        --------------------------------------------

        1. Testing that the get_ticker_data method (and 'get_historical_klines' under the hood) pass through

        2. Special case response shape test:
            '1h' BTC data request on a single must return the expected shape
        """
        try:
            data = self.bw.get_ticker_data(symbol='BTCUSDT',
                                           start_time='2023-01-01',
                                           end_time='2023-01-02',
                                           interval='1h')
        except Exception as e:
            logging.error('An error happened in the get_ticker_data method')
            raise e

        self.assertEqual(first=data.shape,
                         second=BTC_SHAPE,
                         msg="Unexpected dataframe shape returned by the get_ticker_data method")

    def test_convert_timestamp(self):
        """
        Testing the 'BinanceWrapper.convert_timestamp' method
        -----------------------------------------------------

        Testing that the timestamp (UNIX to pd.Timestamp) conversion functions as expected with a numerical example
        """
        try:
            timestamp = self.bw.convert_timestamp(UNIX_TIMESTAMP)
        except Exception as e:
            logging.error('An error happened when trying to convert a timestamp')
            raise e

        # Checking timestamp equality
        self.assertEqual(first=pd.Timestamp(CORRESPONDING_DATETIME),
                         second=timestamp)


if __name__ == '__main__':
    # Launching tests
    unittest.main()
