# loading required libraries
import math # constant "pi" for circle metrics

# creating an abstract base class
class Shape:
    def area(self) -> float:
        pass
    def perimeter(self) -> float:
        pass

# creating a derived class for circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    def area(self) -> float:
        return math.pi * self.radius * self.radius # pi.r^2
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius # 2.pi.r

# creating a derived class for rectangle
class Rectangle(Shape):
    def __init__(self, length: float, breadth: float):
        self.length = length
        self.breadth = breadth
    def area(self) -> float:
        return self.length * self.breadth # l.b
    def perimeter(self) -> float:
        return 2 * (self.length + self.breadth) # 2.(l+b)

# creating a derived class for square
class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

if __name__ == "__main__":
    # creating objects of different classes
    circle = Circle(radius=5)
    rectangle = Rectangle(length=5, breadth=10)
    square = Square(side=5)

    # printing the area of different shapes
    print("Area of circle: {0:.2f}".format(circle.area()))
    print("Area of rectangle: {0:.2f}".format(rectangle.area()))
    print("Area of square: {0:.2f}".format(square.area()))
    
    # printing the perimeter of different shapes   
    print("Perimeter of circle: {0:.2f}".format(circle.perimeter()))
    print("Perimeter of rectangle: {0:.2f}".format(rectangle.perimeter()))
    print("Perimeter of square: {0:.2f}".format(square.perimeter()))