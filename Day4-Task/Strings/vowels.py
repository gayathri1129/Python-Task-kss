Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Write a program to count the number of vowels in a string.
>>> user=input("Enter the string : ")
Enter the string : gayathri bujji
>>> count=0
>>> for letter in user:
...     if letter.lower() in 'aeiou':
...         count+=1
...         print("String count",count)
... 
...         
String count 1
String count 2
String count 3
String count 4
String count 5
>>> print(count)
5
