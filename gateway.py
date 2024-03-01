#!/usr/bin/python3

from flask import Flask, jsonify, request
from utils.utils import parse_arguments
from winance import BinanceWrapper
import logging


"""
Creating the main API gateway providing a service wrapping the Binance API
"""


def create_gateway(public=True):
    """
    Creating the main gateway

    if public is set to False, an api key and secret key will be specified
    """
    # Parsing arguments, setting logging configuration
    arguments = parse_arguments()

    credentials = {
        'api_key': None if public else arguments.api_key,
        'secret_key': None if public else arguments.secret_key
    }

    binance_wrapper = BinanceWrapper(**credentials)

    app = Flask('Binance Wrapper - Gateway Service')

    @app.route('/get_tickers', methods=['GET'])
    def get_tickers():
        """
        Responding with all available tickers
        """
        try:
            tickers = binance_wrapper.get_symbols()
        except Exception as e:
            logging.error(f"An error happened when requesting available tickers : {e}")
            return jsonify({'message': e}), 500

        return jsonify(tickers)

    @app.route('/get_ticker_data/<symbol>/<start_time>/<end_time>/<interval>', methods=['GET'])
    def get_ticker_data(symbol, start_time, end_time, interval):
        """
        Profile suggestion, logic provided by the engine
        """
        # Requesting the data through our Binance wrapper
        try:
            data = binance_wrapper.get_ticker_data(symbol=symbol,
                                                   start_time=start_time,
                                                   end_time=end_time,
                                                   interval=interval)
        except Exception as e:
            logging.error(f"An error happened when executing the following request {request} : {e}")
            return jsonify({'message': e}), 500

        return jsonify(data.to_json())

    @app.route('/get_data/<symbols>/<start_time>/<end_time>/<interval>', methods=['GET'])
    def get_data(symbols, start_time, end_time, interval):
        """
        Profile suggestion, logic provided by the engine
        """
        # Requesting the data through our Binance wrapper
        try:
            data = binance_wrapper.get_data(symbols=symbols,
                                            start_time=start_time,
                                            end_time=end_time,
                                            interval=interval,
                                            gateway=True)
        except Exception as e:
            logging.error(f"An error happened when executing the following request {request} : {e}")
            return jsonify({'message': e}), 500

        return jsonify({symbol: df.to_json() for symbol, df in data.items()})

    # Every request method was defined, returning the application for it to be executed
    logging.info("Successfully created the API gateway")

    return app
