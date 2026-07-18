Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Write a program that takes two numbers and prints their product.
>>> num1=input('Enter the 1st num')
Enter the 1st num10
>>> num2=input('Enter the 2nd num')
Enter the 2nd num20
>>> product=num1*num2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    product=num1*num2
TypeError: can't multiply sequence by non-int of type 'str'
>>> num1=int(input('Enter 1st num'))
Enter 1st num10
>>> num2=int(input('Enter 2nd num'))
Enter 2nd num20
>>> pro=num1*num2
>>> print('product of 2 number is', pro)
product of 2 number is 200
