Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> import pandas as pd
>>> arr = np.array([10, np.nan, 30, np.nan, 50])
>>> S = pd.Series(arr)
>>> mean = S.mean()
>>> KeyboardInterrupt
>>> KeyboardInterrupt
>>> S = S.fillna(mean)
>>> print(S)
0    10.0
1    30.0
2    30.0
3    30.0
4    50.0
dtype: float64
