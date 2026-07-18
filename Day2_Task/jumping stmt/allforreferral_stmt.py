Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,11):
...     if i%2==0:
...         print(i)
... 
...         
2
4
6
8
10
>>> for i in range(1,11):
...     if i%2==0:
...         break
...     print(i)
... 
...     
1
>>> for i in range(1,11):
...     if i%2==0:
...         continue
...     print(i)
... 
...     
1
3
5
7
9
>>> for i in range(1,11);
SyntaxError: incomplete input
>>> for i in range(1,11):
...     if i%2==0:
...         pass
...     print(i)
... 
...     
1
2
3
4
5
6
7
8
9
10
