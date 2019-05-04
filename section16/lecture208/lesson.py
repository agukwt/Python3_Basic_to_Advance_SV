#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import os
import hashlib


user_name = 'user1'
user_pass = 'password'
db = {}

salt = base64.b64encode(os.urandom(32))

def get_digest(password):
    # password = bytes(password, 'utf8')
    # digest = hashlib.sha3_256(salt+password).hexdigest()
    # for _ in range(1000):
    #     digest = hashlib.sha3_256(bytes(digest, 'utf8')).hexdigest()

    return hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf8'), salt, 1000)


def is_login(user_name, password):
    return get_digest(password) == db[user_name]


db[user_name] = get_digest(user_pass)
print(db[user_name].decode('utf8'))
print(is_login(user_name, user_pass))
