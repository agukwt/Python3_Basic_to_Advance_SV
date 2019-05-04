#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

path = r'section11/lecture119/config.yml'

# write
with open(path, 'w', encoding='utf8') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': '80'
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': '3306'
        }
    }, yaml_file, default_flow_style=False)

# read
with open(path, 'r', encoding='utf8') as yaml_file:
    data = yaml.load(yaml_file)
    print(data)
    print(data['web_server']['host'])
