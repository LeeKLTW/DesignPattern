# -*- coding: utf-8 -*-
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self._width}, height: {self._height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @width.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self, size):
        super(Square, self).__init__(size, size)
        # Rectangle.__init__(self, size, size)


    # NOTE: this will make this subclass violate LSP, see use_it()
    @Rectangle.width.setter
    def width(self,value):
        _width = _height = value

    # NOTE: this will make this subclass violate LSP, see use_it()
    @Rectangle.height.setter
    def height(self,value):
        _width = _height = value

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f"Expected an area of {expected}, got {rc.area}")

rc = Rectangle(2,3)
use_it(rc)

sq = Square(5)
use_it(sq)  # LSP violated.