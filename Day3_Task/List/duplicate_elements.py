Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a program to remove duplicate elements from a list
>>> num=[34,45,6,7,7,8,7,76,5,7]
>>> num.sort()
>>> print(num)
[5, 6, 7, 7, 7, 7, 8, 34, 45, 76]
>>> num=list(set(num))
>>> print(num)
[34, 5, 6, 7, 8, 76, 45]
