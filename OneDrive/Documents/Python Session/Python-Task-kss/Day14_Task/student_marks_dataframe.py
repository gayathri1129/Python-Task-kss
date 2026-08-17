Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> data = pd.DataFrame({
...     "Name": ["A", "B", "C"],
...     "Math": [80, 70, 60],
...     "Science": [90, 60, 70]
... })
>>> data["Total"] = data["Math"] + data["Science"]
>>> print(data)
  Name  Math  Science  Total
0    A    80       90    170
1    B    70       60    130
2    C    60       70    130
>>> highest = data.loc[data["Total"].idxmax()]
>>> print(highest)
Name         A
Math        80
Science     90
Total      170
Name: 0, dtype: object
