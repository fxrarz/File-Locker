#!/usr/bin/python3

import jwt
import os

path = "/home/username/location"
os.chdir(path)
with open("closed", "r") as f:
  data = f.read()
  password = input("Enter your password to unlock?\n")
  decoded_jwt = jwt.decode(data, password, algorithms=["HS256"])
with open("open", "w") as f:
  data = f.write(decoded_jwt["encrypted"])
  
os.remove("closed")
