Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> import pandas as pd
>>> S = pd.Series([10, 50, 30, 80, 20])
>>> S[S > 40] = 0
>>> print(S)
0    10
1     0
2    30
3     0
4    20
dtype: int64
