#!/usr/bin/python3

from gateway import create_gateway


if __name__ == '__main__':
    """
    Instantiating the wrapper API service
    """
    gateway = create_gateway()

    gateway.run(debug=True)
