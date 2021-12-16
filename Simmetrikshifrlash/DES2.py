# import Crypto
# from Crypto.PublicKey import RSA
# from Crypto import Random
# import ast
#
# random_generator = Random.new().read
# key = RSA.generate(1024, random_generator) #generate pub and priv key
#
# publickey = key.publickey() # pub key export for exchange
#
# encrypted = publickey.encrypt('encrypt this message', 32)
# #message to encrypt is in the above line 'encrypt this message'
#
# print('encrypted message:', encrypted) #ciphertext
# f = open ('encryption.txt', 'w')
# f.write(str(encrypted)) #write ciphertext to file
# f.close()

#decrypted code below
# decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
#
# print('decrypted', decrypted)
#
# f = open ('encryption.txt', 'w')
# f.write(str(message))
# f.write(str(decrypted))
# # f.close()
# # f = open('encryption.txt', 'r')
# # message = f.read()
# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.PublicKey import RSA
#
# message = b'You can attack now!'
# key = RSA.importKey(b'SALOM')
# cipher = PKCS1_OAEP.new(key)
# ciphertext = cipher.encrypt(message)
# key = RSA.importKey(open('private.pem').read())
# cipher = PKCS1_OAEP.new(key)
# message = cipher.decrypt(ciphertext)
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP


def rsa_encrypt_decrypt():
    key = RSA.generate(2048)
    private_key = key.export_key('PEM')
    public_key = key.publickey().exportKey('PEM')
    print(type(public_key))
    message = input('plain text for RSA encryption and decryption:')
    message = str.encode(message)
    rsa_public_key = RSA.importKey(public_key)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(message)


    print('your encrypted_text is : {}'.format(encrypted_text))


    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(encrypted_text)

    print('your decrypted_text is : {}'.format(decrypted_text))

rsa_encrypt_decrypt()