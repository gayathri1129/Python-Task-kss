Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import copy
>>> classes=[["maths",[30,35]],["sci",[25,28]]]
>>> copied_classes=copy.deepcopy(classes)
>>> classes[0][1][0]=40
>>> print(classes)
[['maths', [40, 35]], ['sci', [25, 28]]]
>>> print(copied_classes)
[['maths', [30, 35]], ['sci', [25, 28]]]
