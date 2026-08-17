Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Write a program that asks the user for their age and prints the age after 5 years
>>> age=input('Enter your age:')
Enter your age:20
>>> future_age=age+5
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    future_age=age+5
TypeError: can only concatenate str (not "int") to str
>>> 
>>> age=int(input('Enter your age:'))
Enter your age:20
>>> future_age=age+5
>>> print('Future age after 5 yrs will be',future_age)
Future age after 5 yrs will be 25
