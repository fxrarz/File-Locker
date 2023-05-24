#!/usr/bin/python3

import jwt
import os

path = "/home/username/location"
os.chdir(path)
with open("open", "r") as f:
  data = f.read()
  password = input("Enter password to lock?\n")
  encoded_jwt = jwt.encode({"encrypted": data}, password, algorithm="HS256")
with open("closed", "w") as f:
  data = f.write(encoded_jwt)
os.remove("open")
