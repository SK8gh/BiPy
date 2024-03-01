## BiPy

When one wants to request cryptocurrency data, a useful tool to use is the Binance Python API.
At start, it can be complicated to use, especially due to the odd format of the returned object.

#### Format comparison
![Binance API request format](https://raw.githubusercontent.com/SK8gh/BiPy/main/documentation/Binance%20request.png)
![BiPy wrapper request format](https://raw.githubusercontent.com/SK8gh/BiPy/main/documentation/Wrapper%20request.png)

This script implements the following components:

- Binance wrapper: Returns the requested data in a clearer format.
- Tests of the wrapper.
- A Flask application implementing a gateway between a requester and the Binance API.
- Gateway tests.


