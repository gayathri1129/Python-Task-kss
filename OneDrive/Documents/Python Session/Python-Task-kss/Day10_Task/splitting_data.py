Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> data=np.array([5,10,15,20,25,30])
>>> parts=np.split(data,3)
>>> print(parts[0])
[ 5 10]
>>> print(parts[1])
[15 20]
>>> print(parts[2])
[25 30]
