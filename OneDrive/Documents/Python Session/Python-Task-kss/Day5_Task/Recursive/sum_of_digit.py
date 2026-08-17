Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Write a recursive function to calculate the sum of digits of a number.
>>> def sum(n):
...     if n==0:
...         return 0
...     return n%10+sum(n // 10)
... 
>>> n=int(input("enter"))
enter123
>>> print(sum(n))
6
