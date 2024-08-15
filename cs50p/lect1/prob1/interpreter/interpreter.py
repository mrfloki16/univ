#!/bin/python3

def main():
  exp = input("Expression : ")
  inter(exp)

def inter(exp):
  x, y, z = exp.split()
  match y:
    case "*":
      print(float(x)*float(z))
    case "+":
      print(float(x)+float(z))
    case "-":
      print(float(x)-float(z))
    case "/":
      print(float(x)/float(z))


main()
