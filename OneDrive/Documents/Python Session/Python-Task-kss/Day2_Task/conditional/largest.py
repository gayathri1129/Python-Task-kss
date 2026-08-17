Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a program to find the largest of three numbers using if-elif-else.
>>> num1=int(input('enter 1st num'))
enter 1st num34
>>> num2=int(input('enter 2nd num'))
enter 2nd num45
>>> num3=int(input('enter 3rd num'))
enter 3rd num34
>>> 
>>> if num1>=num2 and num1>=num3:
...     print('largest',num1)
... elif num2>=num1 and num2>=num3:
...     print('largest', num2)
... else:
...     print('largest',num3)
... 
...     
largest 45
