from Time import *
from Point import *

start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)
print(start + 1337)
print(1337 + start)

p1 = Point(10, 20)
p2 = Point(30, 40)
print(p1 + p2)
print(p1 + (90, 100))
print((90, 100) + p1)
