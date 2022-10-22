class Student:
    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


Badhon = Student()
print(isinstance(Badhon, Student))
Badhon.set_value(201002032, 3.25)
Badhon.display()

Jahid = Student()
print(isinstance(Jahid, Student))
Jahid.set_value(201002463, 3.50)
Jahid.display()
