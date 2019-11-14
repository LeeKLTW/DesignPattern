# -*- coding: utf-8 -*-
class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

    def __repr__(self):
        return f'Singleton_at_{id(self)}'

def test():
    a = Singleton()
    b = Singleton()
    print(a)  # Singleton_at_1234567890
    print(b)  # None
