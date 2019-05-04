#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import requests
import zipfile


with open('a.txt', 'w', encoding='utf8') as f:
    f.write('test test')

with open('a.txt', 'r', encoding='utf8') as f:
    print(f.read())

f = io.StringIO()
f.write('String io test')
f.seek(0)
print(f.read())

f = io.BytesIO()
f.write(b'String io test')
f.seek(0)
print(f.read())



url = 'https://files.pythonhosted.org/packages/ed/69/c805067de1feedbb98c5' \
      '3174b0f2df44cc05e0e9ee73bb85eebc59e508c6/setuptools-41.0.0.zip'

f = io.BytesIO()
r = requests.get(url)
f.write(r.content)

with zipfile.ZipFile(f) as z:
    with z.open('setuptools-41.0.0/README.rst') as r:
        print(r.read().decode())