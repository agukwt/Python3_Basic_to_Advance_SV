#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

s = """\
Hi $name.
$contents
Have a good day
"""

with open('design/email_template.txt', 'r') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)
