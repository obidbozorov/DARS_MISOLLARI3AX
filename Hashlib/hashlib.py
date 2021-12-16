# import hashlib
# # print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)
# hash_object = hashlib.sha224(b'Hello WorlD')
# print("Sha224=",hash_object.hexdigest())
# hash2=hashlib.sha224(b'Hello World')
# print("Sha224=",hash2.hexdigest())
#from hashlib import *
# h1=sha256(b'Hello')
# h1.update(b' World')
# h1.update(b'!')
# print(h1.hexdigest())
# h2=sha256(b'Hello World!')
# print(h2.hexdigest())
import hashlib
file = f"Tkinter.docx"
BLOCK_SIZE = 65536
file_hash = hashlib.sha256()
with open(file, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash.update(fb)
        fb = f.read(BLOCK_SIZE)
print (file_hash.hexdigest())
