Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Write a program to check whether a given number is an Armstrong number or not.
>>> num=int(input('enter the num'))
enter the num153
>>> temp=num
>>> sum=0
>>> while temp>0:
...     digit=temp%10
...     sum=sum+digit**3
...     temp=temp//10
... 
...     
>>> if sum==num:
...     print('Armstrong num')
...     else:
...         
SyntaxError: invalid syntax
>>> if sum==num:
...     print('armstrong')
...     else:
...         
SyntaxError: invalid syntax
>>> if sum==num:
...     print("armstrong")
... else:
...     print('not armstrong')
... 
...     
armstrong
