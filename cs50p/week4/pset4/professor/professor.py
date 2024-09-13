#!/bin/python3

from random import randint

def main():
  level = get_level()
  print(level)
  score = 0
  for i in range(10):
    chance = 0
    equation = []

    for i in range(2):
      equation.append(generate_integer(level))

    for x in range(3):
      rep = input(f"{equation[0]} + {equation[1]} = ")
      if rep == str(equation[0]+equation[1]):
        break
      else:
        print("EEE")
        chance = chance + 1

    if chance == 3:
      print(f"{equation[0]} - {equation[1]} = {(equation[0]+equation[1])}")
    else:
      score = score + 1

  print(f"Score : {score}")
  exit()


def get_level():
  while True:
    try:
      l = [1,2,3]
      i = int(input("Level : "))
      if i in l:
        return i
    except ValueError:
      pass


def generate_integer(level):
  end = []
  start = {
    1: 0,
    2: 10,
    3: 100
  }

  for x in range(level):
    end.append("9")
  num = int("".join(end))
  return randint(start[level], num)


if __name__ == "__main__":
  main()
