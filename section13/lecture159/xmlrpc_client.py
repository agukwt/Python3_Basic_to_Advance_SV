#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpc.client


with xmlrpc.client.ServerProxy('http://127.0.0.1:8000/') as proxy:
    print(proxy.add_num(1015564641, 206441364))
