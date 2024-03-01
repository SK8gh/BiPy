## BiPy

When one wants to request cryptocurrency data, a useful tool to use is the Binance Python API.
At start, it can be complicated to use, especially due to the odd format of the returned object.

### Format comparison
##### Binance request format
<div align="left">
  <img src="https://github.com/SK8gh/BiPy/blob/main/images/Binance%20request.png" width="600">
</div>

##### Wrapper request format
<div align="left">
  <img src="https://github.com/SK8gh/BiPy/blob/main/images/Wrapper%20request.png" width="500">
</div>


<br>
This script implements the following components:

- Binance wrapper: Returns the requested data in a clearer format.
- Tests of the wrapper.
- A Flask application implementing a gateway between a requester and the Binance API.
- Gateway tests.


