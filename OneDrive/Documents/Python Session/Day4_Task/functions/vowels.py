Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #. Write a function that takes a string as input and returns the number of vowels.
>>> def vowels(text):
...     count=0
...     for letter in text:
...         if letter.lower() in 'aeiou':
...             count=count+1
...             return count
... 
...         
>>> text=input('Enter the string')
Enter the string gayathri
>>> res=vowels(text)
>>> print(res)
1
>>> def v(t):
...     count=0
...     for let in t:
...         if let.lower() in 'aeiou':
...             count=count+1
... 
...             
>>> return count
SyntaxError: 'return' outside function
