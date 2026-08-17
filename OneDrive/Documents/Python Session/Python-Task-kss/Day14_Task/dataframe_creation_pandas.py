Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 2. Basic DataFrame Creation from NumPyYou have:data = np.array([[1, 2], [3, 4], [5, 6]])Task:● Convert it into a Pandas DataFrame● Add column names: "X", "Y"
SyntaxError: invalid character '●' (U+25CF)
>>> import numpy as np
>>> import pandas as pd
da
>>> data=np.array([[1,2],[3,4],[5,6]])
>>> df=pd.DataFrame(data,columns=["X","Y"])
>>> print(df)
   X  Y
0  1  2
1  3  4
2  5  6
