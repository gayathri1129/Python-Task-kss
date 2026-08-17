Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Write a program to check whether a number is Prime.
>>> num=int(input('enter the num'))
enter the num13
>>> count=0
>>> for i in range(1,num+1):
...     if num%i==0:
...         count=count+1
... 
...         
>>> if count==2:
...     print('prime num')
... else:
...     print('not a prime num')
... 
...     
prime num
