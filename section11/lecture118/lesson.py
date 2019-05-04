#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser

path = r'section11/lecture118/config.ini'

# write
config = configparser.ConfigParser()
config['DEFAULT'] = {
    'debug': True
}
config['web_server'] = {
    'host': '127.0.0.1',
    'port': 80
}
config['db_server'] = {
    'host': '127.0.0.1',
    'port': 3206
}
with open(path, 'w', encoding='utf8') as config_file:
    config.write(config_file)

# # read
config = configparser.ConfigParser()
config.read(path, encoding='utf8')
print(config.sections())
print([x for x in config['web_server']])
print(config['web_server']['host'])


