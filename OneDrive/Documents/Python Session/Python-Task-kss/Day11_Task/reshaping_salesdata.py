Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> sales = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
>>> arr = np.array(sales)
>>> matrix = arr.reshape(4, 3)
>>> print(matrix)
[[ 10  20  30]
 [ 40  50  60]
 [ 70  80  90]
 [100 110 120]]
