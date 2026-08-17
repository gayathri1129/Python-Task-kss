Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> marks = np.array([
...     [78, 85],
...     [90, 88],
...     [67, 72]
... ])
>>> result = marks[1, 1]
>>> print("Second student's second subject mark:", result)
Second student's second subject mark: 88
