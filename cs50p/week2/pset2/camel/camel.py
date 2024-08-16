#!/bin/python3

def main():
  camel = input("camelCase : ")
  snake(camel)

def snake(camel):
  s = []
  for x in camel:
    match x:
      case x if x.isupper():
        s.append("_")
        s.append(x.lower())
      case _:
        s.append(x)
  snake = "".join(s)
  print(f"snake_case : {snake}")

main()
