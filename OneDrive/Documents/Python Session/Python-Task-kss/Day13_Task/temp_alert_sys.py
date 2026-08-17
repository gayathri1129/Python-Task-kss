Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> temp=np.array([28,32,35,31,29,40,38])
>>> indices=np.where(temp>30)
>>> print(indices[0])
[1 2 3 5 6]
