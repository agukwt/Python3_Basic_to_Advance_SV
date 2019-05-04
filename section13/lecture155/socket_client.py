#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

# TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 50007))
    s.sendall(b'Hello')
    data = s.recv(1024)
    print(repr(data))

# # UDP
# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#     s.sendto(b'Hello UDP', ('localhost', 50007))