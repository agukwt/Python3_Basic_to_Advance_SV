#!/usr/bin/env python
# -*- coding: utf-8 -*-

import contextlib

def is_ok_job():
    try:
        print('do something')
        raise Exception('error')
        return True
    except Exception:
        return False

def cleanup1():
    print('clean up1')
def cleanup2():
    print('clean up2')

# try:
#     is_ok = is_ok_job()
#     print('more tasks')
# finally:
#     if not is_ok:
#         cleanup1()
#         cleanup2()


with contextlib.ExitStack() as stack:
    stack.callback(cleanup1)
    # stack.callback(cleanup2)
    @stack.callback
    def cleanup2():
        print('clean up2')


    is_ok = is_ok_job()
    print('more tasks')

    if is_ok:
        stack.pop_all()
