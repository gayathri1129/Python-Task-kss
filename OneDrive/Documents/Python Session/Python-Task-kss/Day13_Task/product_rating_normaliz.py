Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> rating=np.array([2,3,4,5,1])
>>> minimum=np.min(ratings)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    minimum=np.min(ratings)
NameError: name 'ratings' is not defined. Did you mean: 'rating'?
>>> minimum=np.min(rating)
>>> maximum=np.max(rating)
>>> normalized=(rating-minimum)/(maximum-minimum)
>>> print(normalized)
[0.25 0.5  0.75 1.   0.  ]
