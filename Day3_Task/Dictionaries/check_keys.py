Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a program to check whether a key exists in a dictionary
>>> Marks={'Telugu':89,'English':87,'Maths':67,'social':78}
>>> sub=input('enter the sub name:')
enter the sub name:Telugu
>>> if sub in Marks:
...     print('sub is found:',sub)
... else:
...     print('sub is not found:',sub)
... 
...     
sub is found: Telugu
