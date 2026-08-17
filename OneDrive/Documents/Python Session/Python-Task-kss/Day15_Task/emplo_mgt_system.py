Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class employee:
    def__init__(self,name,salary):
        
SyntaxError: invalid syntax
class emmployee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        
employees={}
try:
    fir i in range(3):
        
SyntaxError: invalid syntax
try:
    for i in range(3):
        name=input("enter the name")
        salary=float(input('enter the salary'))

        employee=emmployee(name,salary)
        employees[name]=employee

except ValueError:
...     print("invlaid salary")
... 
...     
enter the namebujji
enter the salary25000
enter the namekanna
enter the salary45000
enter the namebhagi
enter the salary55556
>>> print("\nEmployees Details")

Employees Details
>>> for name,employee in employees.items():
...     print(employee.name)
...     print(employee.salary)
... 
...     
bujji
25000.0
kanna
45000.0
bhagi
55556.0
>>> try:
...     with open("employees.txt", "w") as file:
...         for name, employee in employees.items():
...             file.write("Name: " + employee.name + "\n")
...             file.write("Salary: " + str(employee.salary) + "\n")
...             file.write("----------------\n")
... 
...     print("\nEmployee data saved successfully.")
... 
... except Exception as e:
...     print("File Error:", e)
... 
...     
File Error: [Errno 13] Permission denied: 'employees.txt'
>>> 
>>> 
