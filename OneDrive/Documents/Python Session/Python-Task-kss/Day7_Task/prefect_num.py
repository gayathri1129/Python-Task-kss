Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Write a program to check whether a number is a Perfect number.
>>> num=int(input('entere the num'))
entere the num6
>>> sum=0
>>> for i in range(1,num):
...     if num%i==0:
...         sum=sum+i
... 
...         
>>> if sum==num:
...     print('perfect num')
... else:
...     print('not prefect num')
... 
...     
perfect num
