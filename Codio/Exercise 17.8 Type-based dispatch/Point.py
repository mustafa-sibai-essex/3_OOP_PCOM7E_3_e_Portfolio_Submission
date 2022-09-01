class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x:{0}, y:{1}'.format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)

        if type(other) is tuple:
            return Point(self.x + other[0], self.y + other[1])

    def __radd__(self, other):
        return self.__add__(other)
