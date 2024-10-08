#!/bin/python3

def main():
  command()

def command():
  total = 0.00
  while True:
    try:
      item = input("Item : ")
      if item.title() in menue:
          total = menue[item.title()] + total
          print(f"Total : ${total:.2f}")
    except ValueError:
      pass
    except EOFError:
      break

menue = {
  "Baja Taco": 4.25,
  "Burrito": 7.50,
  "Bowl": 8.50,
  "Nachos": 11.00,
  "Quesadilla": 8.50,
  "Super Burrito": 8.50,
  "Super Quesadilla": 9.50,
  "Taco": 3.00,
  "Tortilla Salad": 8.00
}

main()
