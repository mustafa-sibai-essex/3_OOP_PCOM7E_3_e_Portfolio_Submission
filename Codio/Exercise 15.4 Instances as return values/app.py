class Point:
    """Represents a point in 2-D space."""


class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """


def print_point(p):
    print("(%g, %g)" % (p.x, p.y))


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

center = find_center(box)
print_point(center)
