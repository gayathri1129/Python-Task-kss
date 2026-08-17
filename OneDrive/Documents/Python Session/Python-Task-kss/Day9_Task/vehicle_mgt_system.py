Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #5. Vehicle Management System (Inheritance)A transport company manages different vehicles. Create a base class Vehicle with attributes like brand and speed. Create derived classes Car and Bike that inherit from Vehicle and display their details.
>>> class vehicle:
...     def __init__(self,brand,speed):
...         self.brand=brand
...         self.speed=speed
... 
...         
>>> class car(vehicle):
...     def dispaly(self):
...         print(self.brand)
...         print(self.speed,"km/h")
... 
...         
>>> class bike(vehicle):
...     def display(self):
...         print(self.brand)
...         print(self.speed,"km/h")
... 
...         
>>> car=car("Toyata",180)
>>> bike("honda",120)
<__main__.bike object at 0x000001D2FFE317F0>
>>> bike=bike("handa",120)
>>> car.display()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    car.display()
AttributeError: 'car' object has no attribute 'display'. Did you mean: 'dispaly'?
>>> car.dispaly()
Toyata
180 km/h
>>> bike.display()
handa
120 km/h
