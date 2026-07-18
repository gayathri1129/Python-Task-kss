Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #write a program to remove duplicate values from a list using a set
>>> num={10,20,30,40,40,50,30,10}
>>> num1=list(set(num))
>>> print(num1)
[50, 20, 40, 10, 30]
