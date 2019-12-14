# -*- coding: utf-8 -*-
# API you are given:
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y


def draw_point(p):
  print('.', end='')


# Code you already have:
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


class LineToPointAdapter(list):
  count = 0

  def __init__(self, line):
    self.count +=1
    print(f'{self.count}: Generating points for line.'
          f'[{line.start.x}, {line.start.y}]→'
          f'[{line.end.x}, {line.end.y}]')
    left = min(line.start.x, line.end.x)
    right = max(line.start.x, line.end.x)
    top = max(line.start.y, line.end.y)
    bottom = max(line.start.y, line.end.y)






