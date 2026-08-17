Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Use modulus operator to check if a number is even or odd.
>>> num=input('Enter the num')
Enter the num4
>>> print(num%2==0)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(num%2==0)
TypeError: not all arguments converted during string formatting
>>> print(int(num%2==0))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(int(num%2==0))
TypeError: not all arguments converted during string formatting
>>> num=int(input('Enter the num'))
Enter the num4
>>> print(num%2==0)
True
>>> num=int(input('Enter the num'))
Enter the num5
>>> prin(num%2==0)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    prin(num%2==0)
NameError: name 'prin' is not defined. Did you mean: 'print'?
>>> print(num%2==0)
False
