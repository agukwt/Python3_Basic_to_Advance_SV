#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):
    def run(self):
        print('first run')


class TeslaCar(Car):
    def __init__(self, model='Model s', enale_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enale_auto_run

    def run(self):
        print('super run')

    def auto_run(self):
        print('auto run')


toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()

tesla_car = TeslaCar('Model s')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()