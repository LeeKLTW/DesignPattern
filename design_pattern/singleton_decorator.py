# -*- coding: utf-8 -*-
import time


def singleton(class_):
  instances = {}

  def get_instance(*args, **kwargs):
    if class_ not in instances:
      instances[class_] = class_(*args, **kwargs)
    return instances[class_]

  return get_instance

@singleton
class Database:
  def __init__(self):
    t = time.time()
    print(f'Call __init__ at {t} with ID  {id(self)}')

if __name__ == '__main__':
  d1 = Database()
  d2 = Database()
  print("Is 2 databases laocate at same ID? ", d1 == d2)

# Note: this will call __init__ once
# Call __init__ at 1575368700.177498 with ID  4504371440
# Is 2 databases laocate at same ID?  True