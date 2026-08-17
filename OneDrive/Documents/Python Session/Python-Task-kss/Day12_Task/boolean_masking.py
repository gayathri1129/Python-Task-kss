Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> salaries=np.array([25000,40000,15000,50000,30000])
>>> above_3000=salaries[salaries>30000]
>>> count=len(above_30000)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    count=len(above_30000)
NameError: name 'above_30000' is not defined. Did you mean: 'above_3000'?
>>> count=len(above_3000)
>>> print(above_3000)
[40000 50000]
>>> print(count)
2
