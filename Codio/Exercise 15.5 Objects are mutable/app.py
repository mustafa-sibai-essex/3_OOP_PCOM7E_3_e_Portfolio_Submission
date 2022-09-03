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


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

center = find_center(box)
print_point(center)

box.width = box.width + 50
box.height = box.height + 100

print("(%g,%g)" % (box.width, box.height))

grow_rectangle(box, 50, 100)
print("(%g,%g)" % (box.width, box.height))


def move_rectangle(rectangle, dx, dy):
    rectangle.corner.x += dx
    rectangle.corner.y += dy


move_rectangle(box, 200, 200)
print("(%g,%g)" % (box.width, box.height))
print("(%g,%g)" % (box.corner.x, box.corner.y))
