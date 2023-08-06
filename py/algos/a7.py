def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    key = key.upper()
    key_len = len(key)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_len]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += char

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    return vigenere_encrypt(ciphertext, key)
