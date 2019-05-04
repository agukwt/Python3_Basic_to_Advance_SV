#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


def worker2(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


def worker3(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


# threadでは以下表記が必要
if __name__ == '__main__':
    d = {'x': 0}
    semaphore = threading.Semaphore(2)
    t1 = threading.Thread(target=worker1, args=(semaphore,))
    t2 = threading.Thread(target=worker2, args=(semaphore,))
    t3 = threading.Thread(target=worker3, args=(semaphore,))
    t1.start()
    t2.start()
    t3.start()
    print('started')
