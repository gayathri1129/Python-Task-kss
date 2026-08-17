Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Create a Number Guessing Game where:
... ● The program generates a random number between 1 and 50 using random.
... ● The user has 5 attempts to guess the number.
... ● After each guess, calculate the absolute difference using math.fabs() and
... display how far the guess is from the correct number
SyntaxError: invalid character '●' (U+25CF)
>>> import random
>>> import math
>>> num= random.randint(1,50)
>>> for i in range(5):
...     guess=int(input('enter the guess:'))
...     if guess==num:
...         print('correct')
...         break
...     else:
...         print("Difference =", math.fabs(guess - num))
... 
...         
enter the guess:20
Difference = 20.0
enter the guess:30
Difference = 10.0
enter the guess:40
correct
