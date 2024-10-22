#!/bin/python3

def main():
  greeding = input("Greeding : ")
  print(f"${value(greeding)}")

def value(x):
  match x.lower().split():
    case x if x[0].startswith("hello"):
      return 0 
    case x if x[0].startswith("h"):
      return 20
    case _:
      return 100

if __name__ == "__main__":
  main()
