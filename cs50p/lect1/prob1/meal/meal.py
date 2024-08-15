#!/bin/python3

def main():
  time = input("What time is it ")
  meal(convert(time))

def convert(time):
  x, y = time.split(":")
  z = float(y)/60
  return float(x)+z

def meal(w):
  match w:
    case w if w >= 7 and w <= 8:
      print("breakfast time")
    case w if w >= 12 and w <= 13:
      print("lunch time")
    case w if w >= 18 and w <= 19:
      print("dinner time")

if __name__ == "__main__":
    main()
