Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a program to calculate the factorial of a number using a loop
>>> n=int(input('enter the num'))
enter the num5
>>> for i in range(1,n+1):
...     fact*=i
...     print(fact)
... 
...     
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    fact*=i
NameError: name 'fact' is not defined
>>> fact=1
>>> for i in range(1,n+1):
...     fact*=i
...     print(fact)
... 
...     
1
2
6
24
120
>>> print('fact=',fact)
fact= 120
