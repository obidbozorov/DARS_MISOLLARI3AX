import hashlib
hash_object = hashlib.sha224(b'Hello World')
print(hash_object.hexdigest())
import hashlib

file = f"1.txt"
BLOCK_SIZE = 65536

file_hash = hashlib.sha256()
with open(file, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash.update(fb)
        fb = f.read(BLOCK_SIZE)

print (file_hash.hexdigest())