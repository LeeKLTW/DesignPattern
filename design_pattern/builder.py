# -*- coding: utf-8 -*-
# In general, in Python this won't be necessary.


class Building:
    # __init__ is defined in here , __init__ specifies the steps needed, and the concrete subclasses implement these steps.
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        return NotImplemented

    def build_size(self):
        return NotImplemented

    def __repr__(self):
        return 'Floor: {0.floor} | Size:{0.size}'.format(self)


class House(Building):
    # __init__ not defined in here
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big'


class Flat(Building):
    # __init__ not defined in here
    def build_floor(self):
        self.floor = 'More than one.'

    def build_size(self):
        self.size = 'Small'


# ref: https://github.com/faif/python-patterns/blob/master/patterns/creational/builder.py
# In some very complex cases, it might be desirable to pull out the building
# logic into another function (or a method on another class), rather than being
# in the base class '__init__'. (This leaves you in the strange situation where
# a concrete class does not have a useful constructor)

class ComplexBuilding:
    # no __init__ here, define another function to build instance
    def __repr__(self):
        try:
            return '[Complex] Floor: {0.floor} | Size:{0.size}'.format(self)
        except:
            try:
                return '[Complex-floor-only] Floor: {0.floor}'.format(self)
            except:
                return '[Complex-size-only] Size:{0.size}'.format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big and fancy'


class ComplexFlat(ComplexBuilding):
    def build_floor(self):
        self.floor = 'More than one.'

    def build_size(self):
        self.size = 'Small and fancy'

def construct_building(cls):
    # cls == class ComplexHouse or ComplexHouseFlat
    building = cls()  # !
    building.build_floor()
    building.build_size()
    return building

def construct_floor_only(cls):
    building = cls()  # !
    building.build_floor()
    return building

def construct_size_only(cls):
    building = cls()  # !
    building.build_size()
    return building



def main():
    house = House()
    flat = Flat()
    print(house)
    print(flat)
    try:
        ch = ComplexHouse()
        print(ch)
    except AttributeError:
        print("AttributeError: 'ComplexHouse' object has no attribute 'size'. Because ComplexHouse.build_floor(), ComplexHouse.build_size() are not called yet.")

    ch = construct_building(ComplexHouse)
    print(ch)
    chfo = construct_floor_only(ComplexHouse)
    print(chfo)
    cfso = construct_size_only(ComplexFlat)
    print(cfso)
