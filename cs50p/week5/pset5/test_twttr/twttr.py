#!/bin/python3

def main():
  phrase = input("Input : ")
  print(f"Output : {shorten(phrase)}")

def shorten(x):
  new = []

  for char in x:
    match char.lower():
      case "a" | "e" | "i" | "o" | "u":
        continue
      case _:
        new.append(char)
  return "".join(new)

if __name__ == "__main__":
  main()
