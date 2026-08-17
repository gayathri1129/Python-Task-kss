Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #9. Online Shopping System (Multilevel Inheritance) An e-commerce company organizes products using multiple levels. Create classes Product → ElectronicProduct → MobilePhone using multilevel inheritance and display product details
>>> class product:
...     def __init__ (self,name,price):
...         self.name=name
...         self.price=price
... 
...         
>>> class electronicproduct(product):
...     def __init__(self,name,price,brand):
...         super().__init__(name,price)
...         self.brand=brand
... 
...         
>>> class mobilephone(electronicproduct):
...     def __init__(self,name,price,brand,storage):
...         super().__init__(name,price,brand)
...         self.storage=storage
...         def display(self):
...             print(self.name)
...             print(self.price)
...             print(self.brand)
...             print(self.storage)
... 
...             
>>> mobile=mobilephone("smartphone",2500,"samsug","128 gb")
>>> mobile.display()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    mobile.display()
AttributeError: 'mobilephone' object has no attribute 'display'
>>> mobile.display()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    mobile.display()
AttributeError: 'mobilephone' object has no attribute 'display'
