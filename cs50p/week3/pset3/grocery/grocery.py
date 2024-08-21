#!/bin/python3

def main():
  grocery()

def grocery():
  d={}
  while True:
    try:
      item = input()
      if item in d:
        d[item] = d[item] + 1
      else:
        d[item] = 1
    except ValueError:
      pass
    except EOFError:
      k = list(d.keys())
      k.sort()
      y = {i: d for i in k}
      for x in y:
        print(f"{d[x]} {x.upper()}")
      break

main()
