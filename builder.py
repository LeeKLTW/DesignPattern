# -*- coding: utf-8 -*-
import abc
class Building:
    def __init__(self):
        self.build_florr()
        self.build_size()

    @abc.abstractmethod
    def build_florr(self):
        return NotImplemented

    @abc.abstractmethod
    def build_size(self):
        return NotImplemented

    def __str__(self):
        return 'Floor: {0.floor} | Size:{0.size}'.format(self)


class House(Building):
    pass

class Flat(Building):
    pass


# ref: https://github.com/faif/python-patterns/blob/master/patterns/creational/builder.py
# In some very complex cases, it might be desirable to pull out the building
# logic into another function (or a method on another class), rather than being
# in the base class '__init__'. (This leaves you in the strange situation where
# a concrete class does not have a useful constructor)

class ComplexBuilding:
    pass

class ComplexHouse(ComplexBuilding):
    pass

def construct_building(cls):
    pass
