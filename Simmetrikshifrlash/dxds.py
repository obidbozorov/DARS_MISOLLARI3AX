# from Crypto.PublicKey import RSA
#
# keyPair = RSA.generate(bits=1024)
# print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
# print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")
# # RSA sign the message
# msg = b'A message for signing'
# from hashlib import sha512
# hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
# signature = pow(hash, keyPair.d, keyPair.n)
# print(type(signature))
# print("Signature:", hex(signature))
# # RSA verify signature
# msg = b'A message for signing'
# hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
# hashFromSignature = pow(signature, keyPair.e, keyPair.n)
# print("Signature valid:", hash == hashFromSignature)
# # RSA verify signature (tampered msg)
# msg = b'A message for signing (tampered)'
# hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
# hashFromSignature = pow(signature, keyPair.e, keyPair.n)
# print("Signature valid (tampered):", hash == hashFromSignature)
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii

# Generate 1024-bit RSA key pair (private + public key)
keyPair = RSA.generate(bits=1024)
pubKey = keyPair.publickey()

# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
msg = b'Message for RSA signing'
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(keyPair)
signature = signer.sign(hash)
print("Signature:", binascii.hexlify(signature))

# Verify valid PKCS#1 v1.5 signature (RSAVP1)
msg = b'Message for RSA signing'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)
try:
    verifier.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")

# Verify invalid PKCS#1 v1.5 signature (RSAVP1)
msg = b'A tampered message'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)
try:
    verifier.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")