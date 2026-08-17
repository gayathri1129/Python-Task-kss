Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> sensor1=np.array([10,20,30])
>>> sensor2=np.array([40,50,60])
>>> combined=np.concatenate((sensor1,sensor2))
>>> print(combined)
[10 20 30 40 50 60]
