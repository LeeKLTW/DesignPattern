# -*- coding: utf-8 -*-
from enum import Enum
from math import *


class CoordinateSystem(Enum):
  CARTESIAN = 1
  POLAR = 2


class Point:
  def __init__(self, a,b, system=CoordinateSystem.CARTESIAN):
    if system == CoordinateSystem.CARTESIAN:
      self.x = a
      self.y = b
    elif system == CoordinateSystem.POLAR:
      self.x = a * sin(b)
      self.y = a * cos(b)

  def __str__(self):
    return f'x: {self.x}, y: {self.y}'

  @staticmethod
  def new_cartesian_point(x, y):
    return Point(x, y)

  @staticmethod
  def new_polar_point(rho, theta):
    return Point(rho * sin(theta), rho * cos(theta))

  class Factory:
    @staticmethod
    def new_cartesian_point(x, y):
      return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
      return Point(rho * sin(theta), rho * cos(theta))


class PointFactory:
  @staticmethod
  def new_cartesian_point(x,y):
    return Point(x,y)

  @staticmethod
  def new_polar_point(rho, theta):
    return Point(rho * sin(theta), rho*cos(theta))

if __name__ == '__main__':
    # method 1
    p1 = Point(2,3,CoordinateSystem.CARTESIAN)
    # method 2
    p2 = PointFactory.new_cartesian_point(1,2)
    # method 3
    p3 = Point.Factory.new_cartesian_point(3,4)
    # method 4
    p4 = Point.new_cartesian_point(5,6)
    print(p1,p2,p3,p4)