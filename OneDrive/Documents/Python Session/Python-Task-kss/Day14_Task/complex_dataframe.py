Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> df = pd.DataFrame({
...     "Name": ["A", "B", "C", "D"],
...     "Marks": [50, 80, 30, 90]
... })
>>> df["Status"] = df["Marks"].apply(lambda x: "Fail" if x < 50 else "Pass")
>>> print(df)
  Name  Marks Status
0    A     50   Pass
1    B     80   Pass
2    C     30   Fail
3    D     90   Pass
>>> passed = df[df["Status"] == "Pass"]
>>> print(passed)
  Name  Marks Status
0    A     50   Pass
1    B     80   Pass
3    D     90   Pass
>>> average = passed["Marks"].mean()
>>> print("\nAverage Marks of Passed Students:", average)

Average Marks of Passed Students: 73.33333333333333
