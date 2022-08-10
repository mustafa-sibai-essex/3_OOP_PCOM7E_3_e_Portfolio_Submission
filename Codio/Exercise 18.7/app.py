from Card import *
from Deck import *
from Hand import *

deck = Deck()

deck.shuffle()
print(deck)
deck.sort()
print('-------')
print(deck)

print('-------')
print('Hand')
print('-------')

hand = Hand('new hand')
print(hand.cards)
print(hand.label)

card = deck.pop_card()
hand.add_card(card)
print(hand)

print('-------')

deck.move_cards(hand, 2)
print(hand)
