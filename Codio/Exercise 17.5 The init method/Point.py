class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def print_point(self):
        print("x:{0}, y:{1}".format(self.x, self.y))
