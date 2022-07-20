import copy


class Point:
    def __init__(self):
        pass


class Rectangle:
    def __init__(self):
        pass


class Circle:
    def __init__(self):
        pass


def point_in_circle(point: Point, circle: Circle):
    x = (point.x - circle.center.x) ** 2
    y = (point.y - circle.center.y) ** 2
    xy = x + y
    radSqr = circle.radius**2
    if xy < radSqr:
        return True
    return False


def rect_in_circle(rect: Rectangle, circle: Circle):

    # Top left corner
    rect_corner = copy.copy(rect.corner)
    if not point_in_circle(rect_corner, circle):
        return False

    # Top right corner
    rect_corner.x += rect.width
    if not point_in_circle(rect_corner, circle):
        return False

    # botom right corner
    rect_corner.y -= rect.height
    if not point_in_circle(rect_corner, circle):
        return False

    # botom left corner
    rect_corner.x -= rect.width
    if not point_in_circle(rect_corner, circle):
        return False

    return True


def rect_circle_overlap(rect: Rectangle, circle: Circle):

    copy_rect = copy.deepcopy(rect)
    copy_circle = copy.deepcopy(circle)

    return not rect_in_circle(copy_rect, copy_circle)


def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == "__main__":
    main()
