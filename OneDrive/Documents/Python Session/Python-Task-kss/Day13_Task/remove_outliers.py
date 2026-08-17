Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> values=np.array([10,12,15,18,100,14,13])
>>> mean=np.mean(values)
>>> std=np.std(values)
>>> print(mean)
26.0
>>> print(std)
30.298514815086232
>>> filtered=values[np.abs(values-mean)<=2*std]
>>> print(filtered)
[10 12 15 18 14 13]
