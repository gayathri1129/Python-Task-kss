Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> prices=[100,200,300]
>>> updated=[]
>>> for price in prices:
...     if price>200:
...         price=price=(price*10/100)
...     else:
...         price=price
...         updated.append(price)
... 
...         
>>> print(updated)
[100, 200]
