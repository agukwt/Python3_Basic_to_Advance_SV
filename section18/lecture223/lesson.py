#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import contextlib


# x = input('Enter:')
# print(x)

# for line in sys.stdin:
#     print(line)

# print('hello')
# sys.stdout.write('hello')
#
# logging.error('error')
# sys.stderr.write('error')

with open('stdout.log', 'w') as f:
    with contextlib.redirect_stdout(f):
        print('hello')
        # help(sys.stdout)

with open('stderr.log', 'w') as f:
    with contextlib.redirect_stderr(f):
        logging.error('error')
