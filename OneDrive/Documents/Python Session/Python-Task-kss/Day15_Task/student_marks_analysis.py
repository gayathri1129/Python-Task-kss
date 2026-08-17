Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> import pandas as pd
>>> marks = np.random.randint(0, 101, 5)
>>> names = ["A", "B", "C", "D", "E"]
>>> df = pd.DataFrame({
...     "Name": names,
...     "Marks": marks
... })
>>> print(pf)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(pf)
NameError: name 'pf' is not defined. Did you mean: 'pd'?
>>> print(df)
  Name  Marks
0    A     72
1    B     18
2    C     60
3    D     67
4    E     10
>>> average = np.mean(df["Marks"])
>>> print(average)
45.4
>>> passed = df[df["Marks"] >= 40]
>>> print("\nPassing Students:")

Passing Students:
>>> for index, student in passed.iterrows():
...     print(student["Name"], "-", student["Marks"])
... 
...     
A - 72
C - 60
D - 67
