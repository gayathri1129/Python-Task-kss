Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 1. Convert NumPy Array to Pandas SeriesA dataset:arr = np.array([10, 20, 30, 40])Task:● Convert this NumPy array into a Pandas Series● Assign index labels: ["A", "B", "C", "D"]
SyntaxError: invalid character '●' (U+25CF)
>>> import numpy as np
>>> import pandas as pd
arr=np.array9[]0
>>> arr=np.array([10,20,30,40])
>>> series=pd.Series(arr,index=["A","B","C","D"])
>>> print(series)
A    10
B    20
C    30
D    40
dtype: int64
