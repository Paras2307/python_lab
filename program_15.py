from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def display(self):
        pass


# Vector class
class Vector(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return 0

    def display(self):
        print(self)

    # Operator overloading for addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Operator overloading for equality
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Operator overloading for less than
    def __lt__(self, other):
        return math.sqrt(self.x**2 + self.y**2) < math.sqrt(other.x**2 + other.y**2)

    # Operator overloading for string representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def display(self):
        print("Circle Radius:", self.radius)
        print("Circle Area:", round(self.area(), 2))


# Main program
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print("First Vector:", v1)
print("Second Vector:", v2)

v3 = v1 + v2
print("Vector Addition:", v3)

print("Are vectors equal?", v1 == v2)
print("Is first vector smaller?", v1 < v2)

c = Circle(5)
c.display()