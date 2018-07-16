#!/usr/bin/python

import sys
import os
import base64
import json

def usage():
  print("usage: ./deserialize.py filename")
  print("")
  print("example: ")
  print("    $ ./serialize.py nike.jpg | ./deserialize.py test.jpg")
  print("")
  sys.exit(1)

if len(sys.argv) == 1:
  usage()

filename = sys.argv[1]

json_str = sys.stdin.read()
d = json.loads(json_str)
img_data_scheme = d["image"]

if img_data_scheme.index(",") >= 0:
  img_base64 = img_data_scheme.split(",")[1]
else:
  img_base64 = img_data_scheme.split(":")[1]
  
img = base64.b64decode(img_base64)

with open(filename, 'wb') as f:
  f.write(img)



