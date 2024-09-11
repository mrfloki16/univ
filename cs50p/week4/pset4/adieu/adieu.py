#!/home/mr_floki/py_venv/bin/python3

import inflect

def main():
  p = inflect.engine()
  name = []
  while True:
    try:
      i = input("Name: ")
      name.append(i)
    except EOFError:
      print(f"Adieu, adieu, to {p.join(name)}")
      exit()

main()
