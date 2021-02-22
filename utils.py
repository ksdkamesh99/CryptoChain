from hashlib import sha256

def hash(string:str):
	return sha256(string.encode('ascii')).hexdigest()
