Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #1. Student Marks AnalysisA teacher stores the marks of 5 students in a NumPy array.Scenario:You are given marks [45, 67, 89, 56, 72].Task:● Convert the list into a NumPy array.● Add 5 grace marks to every student.● Print the updated marks
>>> import numpy as np
>>> marks=[45,67,89,56,72]
>>> mark_array=np.array(marks)
>>> updated_marks=mark_array+5
>>> print(updated_marks)
[50 72 94 61 77]
