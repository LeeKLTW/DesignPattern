# -*- coding: utf-8 -*-
import time


class Database:
  _instance = None

  def __init__(self):
    t = time.time()
    print(f'Call __init__ at {t} with ID  {id(self)}')

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
    return cls._instance


if __name__ == '__main__':
  d1 = Database()
  d2 = Database()
  print("Is 2 databases laocate at same ID? ", d1 == d2)
