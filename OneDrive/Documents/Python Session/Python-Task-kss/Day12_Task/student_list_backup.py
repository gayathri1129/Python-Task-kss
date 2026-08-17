Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #1. Student List Backup (Shallow Copy) A teacher has a list of student marks: marks = [50, 60, 70, 80] Scenario: She creates a backup using assignment:backup = marksTask:● Modify the first element in marks.● Observe the change in backupExplain why both lists are affected.
>>> marks=[50,60,70,80]
>>> backup=marks
>>> marks[0]=100
>>> print(marks)
[100, 60, 70, 80]
>>> print(backup)
[100, 60, 70, 80]
