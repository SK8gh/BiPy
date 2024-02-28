#!/usr/bin/python3

"""
        Defining constants used in the Binance Wrapper testing file
"""

from configuration import RESPONSE_COLUMNS
from datetime import datetime

# These symbols must appear in a get_tickers request
EXPECTED_SYMBOLS = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']

# Expected shape when requesting bitcoin data on a given date and '1h' interval (24 + 1 = 25 rows)
BTC_SHAPE = (25, len(RESPONSE_COLUMNS))

# Test Unix timestamp in milliseconds and corresponding datetime
UNIX_TIMESTAMP, CORRESPONDING_DATETIME = 1704067200000, datetime(year=2024, month=1, day=1)
