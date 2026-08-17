Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
3. Shopping Cart System
... Scenario: A user adds items to a shopping cart.
... Task:
... ● Store items in a list
... ● Convert to set to remove duplicates
... ● Use loop + condition to calculate total cost
... ● Handle invalid input using try-except
... 
SyntaxError: invalid character '●' (U+25CF)
>>> 
>>> items=["apple","banana","apple","milk"]
>>> unique_items=srt(items)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    unique_items=srt(items)
NameError: name 'srt' is not defined. Did you mean: 'set'?
>>> unique_items=set(items)
>>> print(unique_items)
{'apple', 'banana', 'milk'}
>>> prices = {
...     "apple": 50,
...     "banana": 30,
...     "milk": 40
... }
>>> total=0
>>> try:
...     # Calculate total cost
...     for item in unique_items:
...         if item in prices:
...             total = total + prices[item]
...         else:
...             print("Price not available for:", item)
... 
...     print("Total Cost:", total)
... 
... except (TypeError, ValueError) as e:
...     print("Invalid input:", e)
... 
...     
Total Cost: 120
