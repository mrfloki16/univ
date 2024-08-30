#!/bin/python3

from random import choice,randint,shuffle

coin = ["heads", "tails"]
print(coin)
coin = choice(coin)
print(f"choice : {coin}")
print("")

number = []
for x in range(10):
  number.append(x)
print(number)
number = randint(1, 10)
print(f"randint : {number}")
print("")

cards = ["jack", "queen", "king"]
print(cards)
new_cards = []
shuffle(cards)
for card in cards:
  new_cards.append(card)
print(f"shuffle : {new_cards}")
