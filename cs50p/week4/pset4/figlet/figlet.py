#!/home/mr_floki/py_venv/bin/python3

from pyfiglet import Figlet
import sys

def main():
  if check_flag():
    i = input("Input : ") 
    font = Figlet(font=sys.argv[2])
    print(font.renderText(i))
  else:
    i = input("Input : ") 
    font = Figlet(font='slant')
    print(font.renderText(i))

def check_flag():
  flag = ["-f", "--font"]
  font = ["slant", "rectangles", "alphabet"]
  if len(sys.argv) == 3 and sys.argv[1] in flag and sys.argv[2] in font:
    return True
  elif len(sys.argv) == 1:
    return False
  else:
    sys.exit("Invalid usage")

main()
