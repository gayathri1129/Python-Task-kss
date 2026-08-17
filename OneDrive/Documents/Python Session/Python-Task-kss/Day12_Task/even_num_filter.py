Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #. Even Number Filter (List Comprehension)A system stores numbers:nums = [1, 2, 3, 4, 5, 6]Task:● Use list comprehension to create a new list containing only even numbers
>>> num=[1,2,3,4,5,6]
>>> even_num=[num for num in num if num%2==0]
>>> print(even_num)
[2, 4, 6]
