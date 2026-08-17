Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> data=[[1,2,3],[4,5],[6]]
>>> flat_list=[num for sublist in data for num in sublist]
>>> print(flat_list)
[1, 2, 3, 4, 5, 6]
>>> square=[num**2 for num in flat_list if num%2==0]
>>> print(square)
[4, 16, 36]
