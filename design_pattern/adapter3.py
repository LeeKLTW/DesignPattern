# -*- coding: utf-8 -*-
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y


def draw_point(p):
  print('.', end='')


class Line:
  def __init__(self, start, end):
    self.start = start
    self.end = end


class Rectangle(list):
  def __init__(self, x, y, width, height):
    super().__init__()
    self.append(Line(Point(x, y), Point(x + width, y)))
    self.append(Line(Point(x + width, y), Point(x + width, y + height)))
    self.append(Line(Point(x, y, Point(x, y + height))))
    self.append(Line(Point(x, y + height), Point(x + width, y + height)))

