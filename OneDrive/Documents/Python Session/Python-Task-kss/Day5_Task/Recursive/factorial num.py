Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Write a recursive function to calculate the factorial of a number.
>>> def fact(n):
...     if n==1:
...         return 1
...     return n*fact(n-1)
... 
>>> num=int(input("Enter the num"))
Enter the num5
>>> print(num)
5
>>> 
>>> print(fact(num))
120
