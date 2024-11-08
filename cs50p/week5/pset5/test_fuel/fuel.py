#!/home/mr_floki/py_venv/bin/python3

def main():
  while True:
    try:
      x = str(input("Fraction : "))
      print(gauge(convert(x)))
      exit()
    except (TypeError, ValueError, ZeroDivisionError):
      pass

def gauge(y):
  if y < 2:
    return "E"
  elif y > 98:
    return "F"
  else:
    return f"{y}%"

def convert(x):
  y = x.split("/")
  if len(y) == 2 and int(y[1]) == 0:
    raise ZeroDivisionError
  elif len(y) == 2 and int(y[0]) <= int(y[1]):
    return round((int(y[0])/int(y[1]))*100)

if __name__ == "__main__":
  main()
