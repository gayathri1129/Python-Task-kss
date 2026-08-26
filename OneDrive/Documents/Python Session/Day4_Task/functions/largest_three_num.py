Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #. Write a Python program with a function that returns the largest of three numbers.
>>> def larg(a,b,c):
...     if a>=b and a>=c:
...         return a
...     elif b>=a and b>=c:
...         return b
...     else:
...         return c
... 
...     
>>> num1=int(input('enter'))
enter10
>>> num2=int(input('enter'))
enter20
>>> num3=int(input('enter'))
enter30
>>> res=larg(num1,num2,num3)
>>> print(res)
30
