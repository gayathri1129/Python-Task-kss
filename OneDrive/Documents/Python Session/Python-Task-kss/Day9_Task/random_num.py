Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #8. Random Number Generator (Generators)A program is needed to generate numbers for testing purposes. Create a generator function that produces numbers from 1 to N and prints them one by one when iterated.
>>> def gen_num(n):
...     for i in range(1,n+1):
...         yield i
... 
...         
>>> n=5
>>> for num in gen_num(n):
...     print(num)
... 
...     
1
2
3
4
5
