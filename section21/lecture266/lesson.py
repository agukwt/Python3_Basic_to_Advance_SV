#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tasks

result = tasks.build_server.delay()     # バックエンドで管理。次に行く。
print('doing…')
print(result)