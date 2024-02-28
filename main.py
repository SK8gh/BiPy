#!/usr/bin/python3

from datetime import timedelta, datetime
from winance import BinanceWrapper
import pandas as pd


if __name__ == '__main__':
    symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'BNBUSDT', 'ADAUSDT']
    start_time = pd.Timestamp(datetime.today() - timedelta(days=1))
    end_time = pd.Timestamp(datetime.today())
    interval = '1m'

    bw = BinanceWrapper()

    data = bw.get_data(symbols=symbols,
                       start_time=start_time,
                       end_time=end_time,
                       interval=interval)

    bw.get_symbols()
