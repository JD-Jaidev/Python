import random
import string

chars = string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()

random.shuffle(key)

# ENCRYPT

plain_text = input('Enter text you want to encrypt :  ').replace(' ','')
cipher_text = ''

for letter in plain_text:
    ind = chars.index(letter)
    cipher_text += key[ind]

print(f'Your encrypted message is : {cipher_text}')

# DECRYPT

cipher_text = input('Enter text you want to decrypt :  ').replace(' ','')
plain_text = ''

for letter in cipher_text:
    ind = key.index(letter)
    plain_text += chars[ind]

print(f'Your decrypted message is : {plain_text}')
