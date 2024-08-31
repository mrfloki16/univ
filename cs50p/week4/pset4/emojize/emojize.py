#!/home/mr_floki/py_venv/bin/python3

from emoji import emojize

def main():
  i = input("Input : ")
  emoj(i)

def emoj(i):
  if emojize(i) == i:
    print(emojize(i, language='alias'))
  else:
    print(emojize(i))

main()
