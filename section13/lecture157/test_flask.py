#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

r = requests.post(
    'http://127.0.0.1:5000/employee', data={'name': 'jun'})
print(r.text)

r = requests.put(
    'http://127.0.0.1:5000/employee', data={'name': 'jun', 'new_name': 'jack'})
print(r.text)

r = requests.delete(
    'http://127.0.0.1:5000/employee', data={'name': 'jack'})
print(r.text)
