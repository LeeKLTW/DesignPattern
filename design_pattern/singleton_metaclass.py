# -*- coding: utf-8 -*-
import time
class Singleton(type):
  _instances= {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(Singleton,cls).__call__(*args,**kwargs)
    return cls._instances[cls]

class Database(metaclass=Singleton):
  def __init__(self):
    t = time.time()
    print(f'Call __init__ at {t} with ID  {id(self)}')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print("Is 2 databases laocate at same ID? ", d1 == d2)
