#!/bin/python3

def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")

def is_valid(plate):
  if not good_length(plate):
    return False
  elif not first_char(plate):
    return False
  elif not good_num(plate):
    return False
  elif not good_char(plate):
    return False
  else:
    return True

def good_length(s):
  return len(s) < 7 and len(s) > 1

def first_char(s):
  char = [x for x in s]
  for x in range(len(char)):
    if char[x].isnumeric():
      return False
    else:
      return True

def good_num(s):
  num = 0
  char = [x for x in s]
  for x in range(len(char)):
    if char[x] == "0" and num == 0:
      return False
    elif char[x].isnumeric():
      num = num + 1 
    elif char[x].isalpha() and num > 0:
      return False
  return True

def good_char(s):
  char = [x for x in s]
  for x in range(len(char)):
    if char[x].isalpha():
      pass
    elif char[x].isnumeric():
      pass
    else:
      return False
      break
  return True

if __name__ == "__main__":
  main()
