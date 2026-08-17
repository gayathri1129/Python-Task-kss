Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> prices=[499,299,799,199,599]
>>> prices_array=np.array(prices)
>>> sorted_prices=np.sort(prices_array)
>>> print(sorted_prices)
[199 299 499 599 799]
