Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #. Write a program to count the frequency of each character in a string.
>>> text=input("Enter the string: ")
Enter the string: vijayawada
>>> for letter in text:
...     print(letter ,":", text.count(letter))
... 
...     
v : 1
i : 1
j : 1
a : 4
y : 1
a : 4
w : 1
a : 4
d : 1
a : 4
