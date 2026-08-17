Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 3. Accessing Specific Data (Indexing)A Series contains:S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"])Task:● Access values for B and D● Return them as a subse
SyntaxError: invalid character '●' (U+25CF)
>>> 
>>> import pandas as pd

... 
>>> S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"])
>>> res=s[["B","D"]]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    res=s[["B","D"]]
NameError: name 's' is not defined. Did you mean: 'S'?
>>> res=S[["B","D"]]
>>> print(res)
B    200
D    400
dtype: int64
