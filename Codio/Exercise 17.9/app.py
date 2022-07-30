from Time import *
from Point import *


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c]+1
    return d


t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
print(histogram(t))

t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
total = sum([t1, t2, t3])
print(total)
