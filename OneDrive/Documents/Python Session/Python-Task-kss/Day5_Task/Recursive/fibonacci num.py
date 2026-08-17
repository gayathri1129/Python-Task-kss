Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Write a recursive function to find the nth Fibonacci number.
>>> def fib(n):
...     if n<=1:
...         return n
...     return fib(n-1)+fib(n-2)
... 
>>> num=int(input("Enter the num"))
Enter the num5
>>> print(fib(num))
5
