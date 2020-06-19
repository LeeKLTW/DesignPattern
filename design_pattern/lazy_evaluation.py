# -*- coding: utf-8 -*-
import functools

class lazy_property:
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val

def lazy_property2(fn):
    attr = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self,attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)

    return _lazy_property


class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count = 0

    @lazy_property
    def relatives(self):
        relatives = "Many relatives"
        return relatives

    #
    @lazy_property2
    def parents(self):
        self.call_count += 1
        return "Father and mother"

john = Person("John", "Coder")
# Before we access `relatives`

sorted(john.__dict__.items())
john.relatives
sorted(john.__dict__.items())

sorted(john.__dict__.items())
john.parents
sorted(john.__dict__.items())
john.call_count
