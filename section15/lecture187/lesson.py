#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    logging.debug('start')
    time.sleep(6)
    logging.debug('end')


def worker2():
    logging.debug('start')
    time.sleep(1)
    logging.debug('end')


# threadでは以下表記が必要
if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t1.setDaemon(True)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started')
    t1.join()