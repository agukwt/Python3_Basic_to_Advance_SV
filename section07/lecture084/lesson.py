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
    def __init__(self, model='Model s', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # @enable_auto_run.setter
    # def enable_auto_run(self, is_enable):
    #     self._enable_auto_run = is_enable

    def run(self):
        print('super run')

    def auto_run(self):
        print('auto run')


# toyota_car = ToyotaCar('Lexus')
# print(toyota_car.model)
# toyota_car.run()

tesla_car = TeslaCar('Model s')
tesla_car.__enable_auto_run = 'xxxxxxxxxxxxxxx'
print(tesla_car.__enable_auto_run)


class T(object):
    pass

t = T()
t.name = 'Mike'
t.age = 20

print(t.name, t.age)
