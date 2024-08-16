#!/bin/python3

def main():
  phrase = input("Input : ")
  print(f"Output : {twttr(phrase)}")

def twttr(x):
  new = []

  for char in x:
    match char.lower():
      case "a" | "e" | "i" | "o" | "u":
        continue
      case _:
        new.append(char)
  return "".join(new)

main()
