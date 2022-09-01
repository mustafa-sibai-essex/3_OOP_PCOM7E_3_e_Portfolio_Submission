class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x:{0}, y:{1}'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
