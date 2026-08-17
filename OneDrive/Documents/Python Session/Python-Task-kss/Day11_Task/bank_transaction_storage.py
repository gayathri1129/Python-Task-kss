Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> transactions = [1200, 500, 800, 1500]
>>> arr = np.array(transactions)
>>> print("Transactions:", arr)
Transactions: [1200  500  800 1500]
>>> print("Type:", type(arr))
Type: <class 'numpy.ndarray'>
>>> print("Is NumPy ndarray:", isinstance(arr, np.ndarray))
Is NumPy ndarray: True
