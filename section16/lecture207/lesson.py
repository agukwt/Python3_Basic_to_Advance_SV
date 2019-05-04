#!/usr/bin/env python
# -*- coding: utf-8 -*-


import string
import random
import logging

from Crypto.Cipher import AES

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


key = ''.join(random.choice(string.ascii_letters)
              for _ in range(AES.block_size))
logging.debug(key)

iv = ''.join(random.choice(string.ascii_letters)
             for _ in range(AES.block_size))
logging.debug(iv)

# plaintext = 'fanacnnakmacu'

# encrypt
with open('test.txt', 'r', encoding='utf8') as f, open('enc.txt', 'wb') as e:
    plaintext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += chr(padding_length) * padding_length
    cipher_text = cipher.encrypt(plaintext)
    logging.debug(cipher_text)
    e.write(cipher_text)

# decrypt
with open('enc.txt', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypt_text = cipher2.decrypt(f.read())
    logging.debug(decrypt_text[:-decrypt_text[-1]])
    print(decrypt_text[:-decrypt_text[-1]].decode('utf8'))


