Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Print a formatted price value. 
... 
>>> price=199.23
>>> print(f'price=${price:.2f}')
price=$199.23
>>> print(f'price=${:.2f}'.format(price))
SyntaxError: f-string: empty expression not allowed
>>> print(f"price=${price:.2f}".format(price))
price=$199.23
