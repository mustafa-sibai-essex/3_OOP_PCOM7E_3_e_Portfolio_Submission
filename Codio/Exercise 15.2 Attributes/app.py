import math


class Point:
    """Represents a point in 2-D space."""


blank = Point()
blank.x = 3.0
blank.y = 4.0

print(blank)
print(blank.x)
print(blank.y)

print("%g, %g" % (blank.x, blank.y))

distance = math.sqrt(blank.x**2 + blank.y**2)
print(distance)


def print_point(p):
    print("(%g, %g)" % (p.x, p.y))


print_point(blank)


def distance_between_points(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


p1 = Point()
p1.x = 100
p1.y = 50

p2 = Point()
p2.x = 400
p2.y = 300
print(distance_between_points(p1, p2))
