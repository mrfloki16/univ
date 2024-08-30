#!/bin/python3

from sys import exit,argv

if len(argv) < 2:
  exit("Too few arguments")
else:
  name = " ".join(argv[1:])
  print(f"hello, my name is {name}") 
