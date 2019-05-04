#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer

# xml通信（JsonRPCもある）
with SimpleXMLRPCServer(('127.0.0.1', 8000)) as server:

    def add_num(x, y):
        return x + y

    # サーバー側での関数の登録
    server.register_function(add_num, "add_num")

    # サーバーの待ち受け
    server.serve_forever()

