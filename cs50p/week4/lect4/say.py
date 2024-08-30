#!/home/mr_floki/py_venv/bin/python3

import cowsay
import sys

if len(sys.argv) > 1:
  cowsay.cow("hello, " + ' '.join(sys.argv[1:]))
else:
  print("Need an argument!!!")
