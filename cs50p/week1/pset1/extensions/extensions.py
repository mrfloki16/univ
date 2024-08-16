#!/bin/python3

def main():
  file = input("File name : ")
  ext(file)

def ext(x):
  image = ["gif","png"]
  app = ["pdf","txt","zip"]

  match x.lower().split()[-1]:
    case x if x.endswith(".jpg") or x.endswith(".jpeg"):
      print("image/jpeg")
    case x if x.endswith(".txt"):
      print("text/plain")
    case x if x.split(".")[-1] in image:
      print(f"image/{x.split('.')[-1]}")
    case x if x.split(".")[-1] in app:
      print(f"application/{x.split('.')[-1]}")
    case _:
      print("application/octet-stream")
	
main()
