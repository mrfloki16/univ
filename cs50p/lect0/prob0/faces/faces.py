#!/bin/python3

def main():
  x = input()
  faces(x)

def faces(x):
  y = x.replace(":)",'\U0001F642').replace(":(",'\U0001F641')
  print(y)

main()
