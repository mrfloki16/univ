#!/bin/python3

def main():
  hello()
  name = input("Hello, what is your name? ")
  hello(name)

def hello(name="new world"):
  print(f"Hello, "+name.strip().title())

main()
