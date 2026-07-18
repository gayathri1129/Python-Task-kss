Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a program to check if an element exists in a set.
... 
>>> num={1,2,3,4,5,6,7,8,9,10}
>>> res=int(input('enter the num:'))
enter the num:10
>>> if res in num:
...     print('found',res)
... else:
...     print('not found',res)
... 
...     
found 10
