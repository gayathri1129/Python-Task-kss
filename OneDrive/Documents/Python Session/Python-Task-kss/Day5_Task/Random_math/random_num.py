Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #
>>> #. Write a Python program using the random module to generate 10 random integers betweeen 1 and 100 and store them ina a list.print the list
>>> import random
>>> num=[]
>>> for i in range(10):
...     num.append(random.randint(1,100))
... 
...     
>>> print(num)
[35, 67, 46, 4, 77, 7, 88, 94, 19, 64]
