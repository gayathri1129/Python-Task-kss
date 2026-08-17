Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Write a program to check whether a given number is a Strong number.
>>> num=int(input('enter the num'))
enter the num145
>>> temp=num
>>> sum=0
>>> while temp>0:
...     digit=temp%10
...     fact=1
...     for i in range(1,digit+1):
...         fact=fact*i
...         sum=sum+fact
...         temp=temp//10
... 
...         
>>> if sum==num:
...     print('strong num')
... else:
...     print('not strong num')
... 
...     
not strong num
