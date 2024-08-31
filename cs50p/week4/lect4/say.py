#!/home/mr_floki/py_venv/bin/python3

import cowsay
import sys
from sayings import *

if len(sys.argv) > 1:
  name = " ".join(sys.argv[1:])
  cowsay.cow(name)
  hello(name)
  goodbye(name)

else:
  print("Need an argument!!!")
