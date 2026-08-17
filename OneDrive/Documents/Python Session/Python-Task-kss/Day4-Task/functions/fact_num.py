Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #. Write a function that returns the factorial of a number.
>>> def fact(num):
...     fact=1
...     for i in range(1,num+1):
...         fact=fact*i
...         return fact
... 
...     
>>> num=int(input("Enter the num"))
Enter the num5
>>> res=fact(num)
>>> print(res)
1
