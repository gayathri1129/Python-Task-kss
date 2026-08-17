Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> import pandas as pd
>>> arr=np.array([10,25,30,15,40])
>>> s=pd.Series(arr)
>>> filtered=s[s>20]
>>> print(filtered)
1    25
2    30
4    40
dtype: int64
