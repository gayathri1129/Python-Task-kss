Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> import pandas as pd
>>> arr=np.array([12,45,22,67,34])
>>> s=pd.Series(arr)
>>> max=s.max()
>>> print(s)
0    12
1    45
2    22
3    67
4    34
dtype: int64
>>> print("maximum values:",max)
maximum values: 67
