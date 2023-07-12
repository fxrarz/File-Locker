import jwt
import os
import sys

def encrypt(password):
	print("Encrypting a file ...")
	with open("open", "r") as f:
		data = f.read()
		encoded_jwt = jwt.encode({"encrypted": data}, password, algorithm="HS256")
		print(encoded_jwt)
	os.rename("open", "closed")
	with open("closed", "wb") as f:
		data = f.write(encoded_jwt)
		

def decrypt(password):
	print("Decrypting a file ...")
	with open("closed", "r") as f:
		data = f.read()
		decoded_jwt = jwt.decode(data, password, algorithms=["HS256"])
		print(decoded_jwt)
	os.rename("closed", "open")
	with open("open", "w") as f:
		data = f.write(decoded_jwt['encrypted'])
		
if sys.argv[1] == 'enc':
	encrypt(sys.argv[2])
if sys.argv[1] == 'dec':
	decrypt(sys.argv[2])
