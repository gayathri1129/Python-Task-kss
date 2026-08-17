Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> arr=[-5,10,15,-2,20,25,30]
>>> num=np.array(arr)
>>> result=num[(num>0)&(num%2==0)]
>>> print(result)
[10 20 30]
