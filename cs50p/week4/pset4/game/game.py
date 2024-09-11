#!/bin/python3

from random import randint

def main():
  l = level()
  chance = []
  for i in range(l):
    chance.append(i+1)
  num = randint(1,l)
  g = guess(chance, num)

def guess(x, y):
  while True:
    try:
      g = int(input("Guess : "))
      if g == y:
        print("Just right!")
        exit()
      elif g > 0 and g < y:
        print("Too small!")
      elif g > y:
        print("Too large!")
      else:
        pass
    except ValueError:
      pass

def level():
  while True:
    try:
      x = int(input("Level : "))
      if x > 0:
        return x
    except ValueError:
      pass

main()
