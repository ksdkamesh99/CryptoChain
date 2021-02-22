from hashlib import sha256
print(sha256("kamesh".encode('ascii')).hexdigest())