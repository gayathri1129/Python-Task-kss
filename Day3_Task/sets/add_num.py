Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a program to add an element to a set.
... 
>>> num={1,2,3,4,5}
>>> num.add(6,7)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    num.add(6,7)
TypeError: set.add() takes exactly one argument (2 given)
>>> num.add(6)
>>> print(num)
{1, 2, 3, 4, 5, 6}
