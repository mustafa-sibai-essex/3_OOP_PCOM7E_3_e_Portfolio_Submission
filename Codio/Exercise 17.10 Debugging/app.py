from Time import *
from Point import *

p = Point(3, 4)
print(vars(p))


def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

print_attributes(p)