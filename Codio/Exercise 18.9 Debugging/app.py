from Card import *
from Deck import *
from Hand import *


def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty


hand = Hand()
print(find_defining_class(hand, "shuffle"))
