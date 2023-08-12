import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        # Class Implementation

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

class Square:
    def __init__(self, side):
        self. side = side
    
    def area(self):
        return self.side ** 2
    
    def diagonal(self):
        return math.sqrt(2) * self.side
    
    def perimeter(self):
        return 4 * self.side

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width   

def shape_factory(shape_name, *args, **kwargs):
    shapes = {"circle": Circle, "square": Square, "rectangle": Rectangle}
    return shapes[shape_name](*args, **kwargs)

def main():
    # Getting the input from the user
    radius = float(input("Enter radius: "))
    side = float(input("Enter side of the square: "))
    length = float(input("Enter the length of the rectangle: ")) 
    width = float(input("Enter the width of the rectangle: "))   
    # Function Call
    circle = shape_factory("circle", radius)
    square = shape_factory("square", side)
    rectangle = shape_factory("rectangle", length, width)
    # Displaying 
    print(f"Area of Circle: {circle.area():.2f}\nPerimeter of Circle: {circle.circumference():.2f}")
    print(f"Area of Square: {square.area():.2f}\nSquare Perimeter:{square.perimeter():.2f}")
    print(f"Area of Rectangle: {rectangle.area():.2f}")

if __name__ == '__main__':
    main()