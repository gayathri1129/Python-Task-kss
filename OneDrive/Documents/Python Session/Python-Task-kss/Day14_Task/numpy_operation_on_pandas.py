Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> s=pd.Series([5,10,15])
>>> updated=s+5
>>> print(updated)
0    10
1    15
2    20
dtype: int64
