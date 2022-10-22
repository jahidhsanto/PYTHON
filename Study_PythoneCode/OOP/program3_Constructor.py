class Student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


Badhon = Student(201002032, 3.25)
print(isinstance(Badhon, Student))
Badhon.display()

Jahid = Student(201002463, 3.50)
print(isinstance(Jahid, Student))
Jahid.display()
