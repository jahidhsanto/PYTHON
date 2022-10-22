from abc import ABC, abstractmethod


# Abstract Class = that class contains Abstract Methode
# If any class inherited Abstract class then must be use all methode that contains Abstract class
class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    # Abstract Methode = without any statement
    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    # __init__
    # area
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle:", area)


class Rectangle(Shape):
    # __init__
    # area
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle:", area)


s = Shape(20, 30)
s.area()

t1 = Triangle(20, 30)
t1.area()

r1 = Rectangle(20, 30)
r1.area()
