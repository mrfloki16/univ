#!/bin/python3

def main():
  x = fraction()
  y = round(x*100)
  if y < 2:
    print("E")
  elif y > 98:
    print("F")
  else:
    print(f"{y}%")

def fraction():
  while True:
    try:
      x = input("Fraction : ")
      y = x.split("/")
      if len(y) == 2 and int(y[0]) <= int(y[1]):
        return int(y[0]) / int(y[1])
    except (ValueError, ZeroDivisionError):
      pass

main()
