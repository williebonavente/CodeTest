# The Data Encryption Standard (DES) is a symmetric-key block cipher algorithm.
# Implementing DES from scratch is beyond the scope of a minimal example.
# Instead, you can use the 'pycryptodome' library in Python to work with DES encryption.

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def encrypt_des(key, data):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

def decrypt_des(key, encrypted_data):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(encrypted_data)
