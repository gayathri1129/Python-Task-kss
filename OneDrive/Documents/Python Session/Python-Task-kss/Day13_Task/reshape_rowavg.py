Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> data=np.arange(1,13 )
>>> matrix=data.reshape(3,4)
>>> row_avg=np.mean(matrix,axis=1)
>>> print(matrix)
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
>>> print(row_avg)
[ 2.5  6.5 10.5]
