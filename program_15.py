from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def __add__(self, other):
        return self.area() + other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return f"Circle with radius {self.radius}"

# Create objects
c1 = Circle(5)
c2 = Circle(3)

print(c1)
print(c2)

print("Area of Circle 1:", round(c1.area(), 2))
print("Area of Circle 2:", round(c2.area(), 2))

print("Sum of Areas:", round(c1 + c2, 2))
print("Both circles have equal area:", c1 == c2)
print("Circle 1 is smaller than Circle 2:", c1 < c2)