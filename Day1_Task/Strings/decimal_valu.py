Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Display a floating number with 2 decimal places.
>>> a=567.7655
>>> print(f'{a:.2f}')
567.77
>>> print(f'{a:.3f})
...       
SyntaxError: incomplete input
>>> print(f'{a:.3f}')
...       
567.765
