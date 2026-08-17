Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #. Write a program to find the second largest number in a list.
... 
>>> num=[5,6,7,8,88,6,55,4,23,5]
>>> num.sort()
>>> print(num)
[4, 5, 5, 6, 6, 7, 8, 23, 55, 88]
>>> print(num[-2])
55
