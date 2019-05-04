#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.server
import socketserver

# TCP
with socketserver.TCPServer(('localhost', 8000),
                            http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()

# # webbrowser
# Terminal
# python >>>
# import webbrowser
# webbrowser.open('localhost:8000')
