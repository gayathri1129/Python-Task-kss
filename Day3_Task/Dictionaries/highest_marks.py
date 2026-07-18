Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #8. Write a program to find the student with the highest marks from a dictionary
>>> student={'Gayathri':89,'Jyothi':87,'Bhagi':67,'Srinu':78}
>>> marks=max(student.get())
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    marks=max(student.get())
TypeError: get expected at least 1 argument, got 0
>>> marks=max(student,key=student.get)
>>> print('hightest',marks)
hightest Gayathri
>>> 
>>> print('marks',student[marks])
marks 89
