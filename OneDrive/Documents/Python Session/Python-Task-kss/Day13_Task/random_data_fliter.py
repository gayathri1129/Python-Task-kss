Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> nums=np.random.randint(1,100,10)
>>> print(num)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(num)
NameError: name 'num' is not defined. Did you mean: 'nums'?
>>> print(nums)
[65  8 68 94 29 21 18 85 57 42]
>>> filtered=nums[nums%5==0]
>>> result-np.sort(filtered)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    result-np.sort(filtered)
NameError: name 'result' is not defined
>>> result=np.sort(filtered)
>>> print(result)
[65 85]
