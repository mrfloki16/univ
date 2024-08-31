#!/home/mr_floki/py_venv/bin/python3

import json
import requests
import sys

if len(sys.argv) != 2:
  print("argv should equal weezer")
  sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
  print(result["trackName"])
