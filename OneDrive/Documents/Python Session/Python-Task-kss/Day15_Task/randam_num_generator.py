Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Scenario:
A system generates random numbers for testing.
Task:
● Use random to generate 10 numbers
● Store in a list
● Use loop + condition to count even/odd numbers
● Use set to remove duplicates

SyntaxError: invalid character '●' (U+25CF)
>>> import random
>>> numbers=[]
>>> for i in range(10):
...     numbers.append(random.randint(1,50))
...     print(numbers)
... 
...     
[14]
[14, 16]
[14, 16, 6]
[14, 16, 6, 37]
[14, 16, 6, 37, 37]
[14, 16, 6, 37, 37, 9]
[14, 16, 6, 37, 37, 9, 45]
[14, 16, 6, 37, 37, 9, 45, 5]
[14, 16, 6, 37, 37, 9, 45, 5, 40]
[14, 16, 6, 37, 37, 9, 45, 5, 40, 36]
>>> for i in range(10):
...     numbers.append(random.randint(1,50))
... 
...     
>>> print(numbers)
[14, 16, 6, 37, 37, 9, 45, 5, 40, 36, 13, 45, 17, 3, 17, 14, 39, 24, 17, 36]
>>> even=0
>>> odd=0
>>> for num in numbers:
...     if num%2==0:
...         even=even+1
...     else:
...         odd=odd+1
... 
...         
>>> print(even)
8
>>> print(odd)
12
>>> unique_num=set(numbers)
>>> print(unique_num)
{3, 36, 37, 6, 5, 40, 9, 39, 45, 14, 13, 16, 17, 24}
