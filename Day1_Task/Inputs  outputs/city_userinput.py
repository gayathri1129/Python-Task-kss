Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Take a user's city name and print: "You live in ___".
>>> city=input('Enter your city name')
Enter your city namevijayawada
>>> print(f"your live in"{city})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(f"your live in",{city})
your live in {'vijayawada'}
>>> print('your live in ',city)
your live in  vijayawada
