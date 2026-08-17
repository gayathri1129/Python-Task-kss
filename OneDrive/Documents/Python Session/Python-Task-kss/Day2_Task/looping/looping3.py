Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #. Write a program to find the sum of numbers from 1 to N using a loop.
>>> 
>>> n=int(input('enter the num'))
enter the num4
>>> sum=0
>>> for i in range(1,n+1)
SyntaxError: incomplete input
>>> for i in range(1,n+1):
...     sum+=i
...     print(sum)
... 
...     
1
3
6
10
>>> print('the sum of sum:',sum)
the sum of sum: 10
>>> n=int(input('enter the num'))
enter the num5
>>> sum=0
>>> for i in range(1,n+1)
SyntaxError: incomplete input
>>> for i in range(1,n+1):
...     sum+=i
...     print('the sum of num:'sum)
...     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('the sum of num',sum)
the sum of num 0
