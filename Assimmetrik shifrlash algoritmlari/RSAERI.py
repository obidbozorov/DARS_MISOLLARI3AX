from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
# Generate 1024-bit RSA key pair (private + public key)
keyPair = RSA.generate(bits=2048)# Maxfiy saqlaydi
pubKey = keyPair.publickey() # Hammaga e'lon qilinadi
msg = b'Axborot xavfsizligi'
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(keyPair)
signature = signer.sign(hash)
print("ERI:", binascii.hexlify(signature))
#----Ikkinchi tomon(QABUL QILUVCHI)
inputmsg = b'Kompyuter tarmoqlari'
hash = SHA256.new(inputmsg)
verifier = PKCS115_SigScheme(pubKey)
try:
    verifier.verify(hash, signature)
    print("ERI to'g'ri")
except:
    print("Ma'lumot soxtalashtirilgan. Imzo noto'g'ri")


