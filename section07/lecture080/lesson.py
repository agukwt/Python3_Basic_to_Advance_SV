#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self, name='mike'):
        self.name = name
        print(self.name)

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run ' * 10)

    def __del__(self):
        print('good bye')



person = Person('skys')
person.say_something()

print('------------------------')