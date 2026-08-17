Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> import pandas as pd
a
>>> arr = np.array([
...     [80, 90],
...     [70, 60],
...     [85, 95]
... ])
>>> df = pd.DataFrame(arr, columns=["Math", "Science"])
>>> df["Total"] = df["Math"] + df["Science"]
>>> print(df)
   Math  Science  Total
0    80       90    170
1    70       60    130
2    85       95    180
>>> highest = df["Total"].idxmax()
>>> print(df.loc[highest])
Math        85
Science     95
Total      180
Name: 2, dtype: int64
