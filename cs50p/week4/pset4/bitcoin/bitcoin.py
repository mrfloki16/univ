#!/home/mr_floki/py_venv/bin/python3

import requests
import sys
import json

def main():
  check_argv()
  usd_price = json_req()["bpi"]["USD"]["rate"]
  final_price = float(sys.argv[1]) * float(usd_price.replace(',',''))
  print(f"${final_price:,.4f}")
  exit()

def json_req():
  try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json") 
    return response.json()
  except requests.RequestException:
    pass

def check_argv():
  if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
  else:
    try:
      if float(sys.argv[1]):
        return True
    except ValueError:
      sys.exit("Command-line argument is not a number")

main()
