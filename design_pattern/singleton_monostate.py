# -*- coding: utf-8 -*-

class CEO:
  __shared_state = {
    'name': 'Steve',
    'age': 55
  }

  def __init__(self):
    self.__dict__ = self.__shared_state

  def __str__(self):
    return f'{self.name} is {self.age} years old.'

class Monostate:
  _shared_state = {}

  def __new__(cls, *args, **kwargs):
    obj = super(Monostate, cls).__new__(cls,*args,**kwargs)
    obj.__dict__ = cls._shared_state
    return obj

