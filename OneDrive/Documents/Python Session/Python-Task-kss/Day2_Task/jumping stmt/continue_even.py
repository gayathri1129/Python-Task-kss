Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #. Write a program that prints numbers from 1 to 10 but skips even numbers using continue
>>> for i in range(1,11):
...     if i%2==0:
...         continue
...     print(i)
... 
...     
1
3
5
7
9
