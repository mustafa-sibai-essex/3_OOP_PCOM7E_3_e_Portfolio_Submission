from Point import *


class Rectangle:
    def __init__(self, position: Point, size: Point):
        self.position = position
        self.size = size
        self.topLeftCorner = Point(position.x, position.y)
        self.topRightCorner = Point(position.x + size.x, position.y)
        self.bottomRightCorner = Point(position.x + size.x, position.y - size.y)
        self.bottomLeftCorner = Point(position.x, position.y - size.y)
