Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> import pandas as pd
>>> names = np.array(["A", "B", "C"])
>>> marks = np.array([80, 90, 70])
>>> df = pd.DataFrame({
...     "Name": names,
...     "Marks": marks
... })
>>> print(df)
  Name  Marks
0    A     80
1    B     90
2    C     70
>>> filtered = df[df["Marks"] > 75]
>>> print(filtered)
  Name  Marks
0    A     80
1    B     90
