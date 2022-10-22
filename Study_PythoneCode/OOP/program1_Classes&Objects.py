class Student:
    roll = ""
    gpa = ""


Badhon = Student()
print(isinstance(Badhon, Student))
Badhon.roll = 201002032
Badhon.gpa = 3.25
print(f"Roll: {Badhon.roll}, GPA: {Badhon.gpa}")

Jahid = Student()
print(isinstance(Jahid, Student))
Jahid.roll = 201002463
Jahid.gpa = 3.50
print(f"Roll: {Jahid.roll}, GPA: {Jahid.gpa}")