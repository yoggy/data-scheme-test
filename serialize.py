#!/usr/bin/python

import sys
import os
import base64
import json

def usage():
  print("usage: ./serialize.py filename")
  print("")
  print("example: ")
  print("    $ ./serialize.py nike.jpg | less")
  print("")
  sys.exit(1)

if len(sys.argv) == 1:
  usage()

filename = sys.argv[1]
root, ext = os.path.splitext(filename)
ext = ext.lower()

with open(filename, 'r') as f:
  img = f.read()
  img_base64 = base64.b64encode(img)

  if ext == ".jpeg" or ext == ".jpg":
    header = "data:image/jpeg;base64,"
  elif ext == ".png":
    header = "data:image/png;base64,"
  elif ext == ".gif":
    header = "data:image/gif;base64,"
  else:
    header = "data:"

  d = {}
  d["image"] = header + img_base64

  json_str = json.dumps(d)

  print(json_str)


