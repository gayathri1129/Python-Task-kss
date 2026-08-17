Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> codes = np.array([2, 4, 1, 4, 3, 4, 5])
>>> indexes = np.where(codes == 4)
>>> print("Indexes of value 4:", indexes[0])
Indexes of value 4: [1 3 5]
