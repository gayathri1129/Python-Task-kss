Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd

... 
>>> S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
>>> S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])
>>> total=S1+S2
>>> total_sales=total.sum()
>>> print(total)
apple     15
banana    35
cherry    55
dtype: int64
>>> print(total_sales)
105
