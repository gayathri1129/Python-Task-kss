Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #. Write a program to check whether an element exists in a tuple
>>> tup=(10,20,30,40,50,60)
>>> num=int(input('enter the value'))
enter the value40
>>> if num in tup:
...     print("found",tup)
... else:
...     print("Not foound",tup)
... 
...     
found (10, 20, 30, 40, 50, 60)
>>> if num in tup:
...     print("found",num)
... else:
...     print("Not foound",num)
... 
found 40
