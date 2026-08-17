Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Write a recursive function to reverse a string.
>>> def rev(s):
...     if s=="":
...         return ""
...     return rev(s[1:])+s[0]
... 
>>> text=input('enter')
enterhello
>>> print(rev(text))
olleh
