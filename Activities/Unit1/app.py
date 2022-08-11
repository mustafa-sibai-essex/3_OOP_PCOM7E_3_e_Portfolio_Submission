# e-Portfolio Activities
# Develop a Python program and apply protected and unprotected variables within it.
#--------------------------------------------------------------------------------------
# In this program, I have created two classes. A parent class called Shape which represents a shape that
# has both length and width as protected variables. The class also has a function that prints those dimensions.
# The Shape class has A child class called Rectangle, which inherits from Shape. The Rectangle class calls the
# base class (Shape) constructor. The Rectangle class has a function called calculatArea, which prints out
# the area of the Rectangle.


class Shape:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def printDimensions(self):
        print("Length:", self._length)
        print("width:", self._width)


class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self, length, width)

    def calculateArea(self):
        print("Rectangle area:", self._length * self._width)


rect = Rectangle(100, 25)
rect.printDimensions()
rect.calculateArea()
