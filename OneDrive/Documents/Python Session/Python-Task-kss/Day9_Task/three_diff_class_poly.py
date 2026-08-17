Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #A graphics application needs to calculate the area of different shapes. Create classes Circle, Rectangle, and Triangle, each having an area() method. Demonstrate polymorphism by calling the same method for different objects.
>>> class circle:
...     def area(self):
...         r=5
...         print("circle area=",3.14*r*r)
... 
...         
>>> class rectangle:
...     def area(self):
...         l=4
...         w=10
...         print("rectangle area=",l*w)
... 
...         
>>> class triangle:
...     def area(self):
...         b=5
...         h=7
...         print("triangle area=",0.5*b*h)
... 
...         
>>> c=circle()
>>> r=rectangle()
>>> t=triangle()
>>> 
>>> c.area()
circle area= 78.5
>>> t.area()
triangle area= 17.5
>>> r.area()
rectangle area= 40
