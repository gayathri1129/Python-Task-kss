Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> matrix=np.random.randint(0,51,(3,3))
>>> print("matrix:")
matrix:
>>> print(matrix)
[[ 3 34 23]
 [38  6 42]
 [27 41 25]]
>>> filtered=matrix[matrix>25]
>>> print(filtered)
[34 38 42 27 41]
