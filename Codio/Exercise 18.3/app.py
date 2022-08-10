from Card import *
from Time import *

card1 = Card(2, 12)
card2 = Card(2, 11)

print(card1)
print(card2)

if card1 < card2:
    print('card1 < card2')

t1 = Time(8, 44, 20)
t2 = Time(8, 55, 10)

if t1 < t2:
    print('t1 < t2')
