Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
>>> S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
>>> res=S1+S2
>>> print(res)
a     NaN
b    25.0
c    45.0
d     NaN
dtype: float64
>>> final_res=res.fillna(0)
>>> print(final_res)
a     0.0
b    25.0
c    45.0
d     0.0
dtype: float64
