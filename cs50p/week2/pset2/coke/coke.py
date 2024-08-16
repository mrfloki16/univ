#!/bin/python3

def main():
  insert_coin()

def insert_coin():
  coke = 50
  while coke > 0:
    coin = input("Insert Coin : ")
    if balance(coin):
      coke = coke - int(coin)
      print(f"Amount Due: {coke}")
    else:
      print(f"Amount Due: {coke}")
  print(f"Change Owed: {abs(coke)}")

def balance(coin):
  match coin:
    case "25" | "10" | "5":
      return True
    case _:
      return False

main()
