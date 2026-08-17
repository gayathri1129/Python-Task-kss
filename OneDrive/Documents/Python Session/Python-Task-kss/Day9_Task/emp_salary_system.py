Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #. Employee Salary System (Simple Inheritance)A company has two types of employees: Employee and Manager. Create a base classEmployee containing name and salary . Create a derived class Manager that inherits from Employee and displays the employee details.
>>> class employee:
...     def__init__(self,name,salary):
...         
SyntaxError: invalid syntax
>>> class emp:
...     def __init__ (self,name,salary):
...         self.name=name
...         self.salary=salary
... 
...         
>>> class manager(emp):
...     def display(self):
...         print(self.name)
...         print(self.salary)
... 
...         
>>> m=manager("gayathri",5000)
>>> m.display()
gayathri
5000
>>> 
