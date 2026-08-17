Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
sales=
>>> sales=np.array([12000,18000,9000,22000,15000,30000])
>>> avg=np.mean(sales)
>>> print(avg)
17666.666666666668
>>> filtered_sales=sales[sales>avg]
>>> print(filtered_sales)
[18000 22000 30000]
