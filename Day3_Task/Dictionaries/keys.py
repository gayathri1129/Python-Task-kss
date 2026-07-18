Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a program to print all keys of a dictionary
>>> frt={'veg':'patato','nonveg':'chicken','friut':'banana','city':'vijayawada'}
>>> print(frt.key())
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(frt.key())
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> print(frt.keys())
dict_keys(['veg', 'nonveg', 'friut', 'city'])
