Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> df = pd.DataFrame({
...     "Price": [100, 200, 300]
... })
>>> df["Discount"] = df["Price"] * 10 / 100
>>> df["Final Price"] = df["Price"] - df["Discount"]
>>> print(df)
   Price  Discount  Final Price
0    100      10.0         90.0
1    200      20.0        180.0
2    300      30.0        270.0
