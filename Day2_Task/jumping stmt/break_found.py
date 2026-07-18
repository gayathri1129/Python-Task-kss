Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a program that searches for a number in a list and breaks the loop when found.
... 
>>> number=[10, 20, 30, 40, 50, 60]
>>> search=int(input('the  enter num'))
the  enter num30
>>> for i in number:
...     if i==search:
...         print("found")
...         break
... else:
...     print('not found')
... 
...     
found
