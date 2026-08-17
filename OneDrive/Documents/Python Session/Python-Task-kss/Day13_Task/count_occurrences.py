Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> data=np.array([1,2,2,3,1,4,2,3])
>>> numbers,counts=np.unique(data,return_counts=True)
>>> print(numbers)
[1 2 3 4]
>>> print(counts)
[2 3 2 1]
