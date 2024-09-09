#!/bin/python3

def main():
  print("Calculation of your salary from now in years.")
  salary = input("Salary : ")
  years = input("Years : ")
  percent = input("Percent : ")

  for x in range(int(years)):
    salary = round(float(salary) * (float(percent)/100+1), 4)

  print(f"Salary in {years} years = {salary}")

main()
