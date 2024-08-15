#!/bin/python3

def main():
  greeding = input("Greeding : ")
  bank(greeding)

def bank(x):
  match x.lower().split():
    case x if x[0].startswith("hello"):
      print("$0")
    case x if x[0].startswith("h"):
      print("$20")
    case _:
      print("$100")

main()
