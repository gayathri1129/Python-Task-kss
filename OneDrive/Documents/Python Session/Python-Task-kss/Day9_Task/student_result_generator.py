Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #7. Student Result Generator (Method Overloading Concept)A school system calculates student results differently depending on available data.Create a Result class where a method can calculate the result using either twosubjects or three subjects.
>>> class result:
...     def calc(self,mark1,mark2,mark3=None):
...         if mark3 is None:
...             total=mark1+mark2
...             aveg=total/2
...         else:
...             total=mark1+mark2+mark3
...             aveg=total/3
...             print(total)
...             print(aveg)
... 
...             
>>> r=result()
>>> r.calc(80,90)
>>> print()

>>> r.calc(80,90,70)
240
80.0
>>> 
