#!/bin/python3

def main():
  date = verify_date()
  print(date)

def verify_date():
  while True:
    try:
      date = input("Date : ")
      if m_d_y(date):
        return m_d_y(date)
      elif m_d_y_v2(date):
        return m_d_y_v2(date)
    except ValueError:
      pass

def m_d_y(date):
  d = "".join(date.split())
  d = d.split("/")
  if len(d) == 3 and int(d[0]) < 13 and int(d[1]) < 32:
    return f"{d[2]}-{d[0].zfill(2)}-{d[1].zfill(2)}"

def m_d_y_v2(date):
  if "," not in date:
    return False
  d = " ".join(date.split(","))
  d = d.split()
  if d[0] in month and int(d[1]) < 32:
    return f"{d[2]}-{month[d[0]]}-{d[1].zfill(2)}"

month = {
  "January":"01",
  "February":"02",
  "March":"03",
  "April":"04",
  "May":"05",
  "June":"06",
  "July":"07",
  "August":"08",
  "September":"09",
  "October":"10",
  "November":"11",
  "December":"12"
}

main()
