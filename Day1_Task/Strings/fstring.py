Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Use **f-strings** to print a sentence with variables.
>>> name='gayathri'
>>> age=24
>>> print(f'my name is {}and age is {}'.format(name,age))
SyntaxError: f-string: empty expression not allowed
>>> print(f'My name is {name}and age is {age}')
My name is gayathriand age is 24
