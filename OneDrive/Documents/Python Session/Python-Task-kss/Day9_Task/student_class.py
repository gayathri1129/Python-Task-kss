class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)
        print()

s1 = Student("Rahul", 101, 85)
s2 = Student("Anita", 102, 90)
s3 = Student("Ravi", 103, 78)

s1.display()
s2.display()
s3.display()
