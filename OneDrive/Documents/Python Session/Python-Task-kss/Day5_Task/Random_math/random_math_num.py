Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Write a Python program that generates 20 random numbers between 1 and 200 using
... the random module and store them in a list.
... Then using the math module, compute and display:
... ● Maximum value
... ● Minimum value
... ● Square root of the maximum number
... ● Logarithm of the minimum number
SyntaxError: invalid character '●' (U+25CF)
>>> 
>>> import random
>>> import math
>>> num=[]
>>> for i in range(20):
...     num.append(random.randint(1,200))
... 
...     
>>> print(num)
[116, 28, 162, 70, 129, 105, 17, 159, 192, 178, 61, 114, 164, 164, 173, 176, 1, 141, 36, 22]
>>> print(max(num))
192
>>> print(min(num))
1
>>> print(math,sqrt(max(num)))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(math,sqrt(max(num)))
NameError: name 'sqrt' is not defined
>>> print(math.sqrt(max(num)))
13.856406460551018
>>> print(math.log(min(num)))
0.0
