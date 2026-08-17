Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
1. Student Score Processor
Scenario:
A teacher stores student names and marks in a list of tuples.
Task:
● Convert data into a dictionary
● Use a loop + condition to find students scoring above 50
● Use math module to calculate average
● Store results in a text file
SyntaxError: invalid character '●' (U+25CF)
import math
student=[("A",60),("B",35),("C",75),("D",40),("E",80)]
student_dict=dict(student)
print(student_dict)
{'A': 60, 'B': 35, 'C': 75, 'D': 40, 'E': 80}
>>> above_50=[]
>>> for name,marks in student_dict.items():
...     if marks>50:
...         above_50.append(name)
... 
...         
>>> print(above_50)
['A', 'C', 'E']
>>> total=sum(student_dict.values())
>>> avg=math.fsum(student_dict.value())/len(student_dict)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    avg=math.fsum(student_dict.value())/len(student_dict)
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
>>> average = math.fsum(student_dict.values()) / len(student_dict)
>>> print(avg)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(avg)
NameError: name 'avg' is not defined
>>> priny(average)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    priny(average)
NameError: name 'priny' is not defined. Did you mean: 'print'?
>>> print(average)
58.0
>>> with open("student_result.txt","w")as file:
...     file.write("student score results\n")
...     file.write(".........................\n")
...     file.write(str(above_50)+"\n")
...     file.write("Average Marks: " + str(average) + "\n")
...     print("Results saved to student_results.txt")
... 
...     
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    with open("student_result.txt","w")as file:
PermissionError: [Errno 13] Permission denied: 'student_result.txt'
