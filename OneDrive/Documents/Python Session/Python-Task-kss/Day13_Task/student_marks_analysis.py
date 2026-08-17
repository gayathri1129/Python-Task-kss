Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> marks=np.array([[70,80,90],[60,75,85],[50,65,70],[90,95,85],[40,55,60]])
>>> total_marks=np.sum(marks,axis=1)
>>> class_avg=np.mean(total_marks)
>>> above_avg=total_marks[total_marks>class_avg]
>>> print(total_marks)
[240 220 185 270 155]
>>> print(class_avg)
214.0
>>> print(above_avg)
[240 220 270]
