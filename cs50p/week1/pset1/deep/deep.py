#!/bin/python3

def main():
  x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
  deep(x)

def deep(x):
  match x.strip().lower():
    case "42" | "forty two" | "forty-two":
      print("yes")
    case _:
      print("No")

main()
