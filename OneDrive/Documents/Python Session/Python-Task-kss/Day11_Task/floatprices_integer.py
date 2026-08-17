Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> prices = np.array([10.5, 20.8, 15.3])
>>> integer_prices = prices.astype(int)
>>> print("Original Prices:", prices)
Original Prices: [10.5 20.8 15.3]
>>> print("Integer Prices:", integer_prices)
Integer Prices: [10 20 15]
