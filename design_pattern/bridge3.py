# -*- coding: utf-8 -*-
from abc import ABC
import unittest

class Shape:
    def __init__(self):
        self.name = None


class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.name = 'Triangle'


class Square(Shape):
    def __init__(self):
        super().__init__()
        self.name = 'Square'


class VectorSquare(Square):
    def __str__(self):
        return f'Drawing {self.name} as lines'


class RasterSquare(Square):
    def __str__(self):
        return f'Drawing {self.name} as pixels'

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

class Shape(ABC):
    def __int__(self, renderer, name):
        self.renderer = renderer
        self.name = name

    def __str__(self):
        return f"Drawing {self.name} as {self.renderer.what_to_render_as}"


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Square')

class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'

class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'

class Evalueate(unittest.TestCase):
    def test_square_vector(self):
        sq = Square(VectorRenderer())
        self.assertEqual(str(sq), 'Drawing Square as lines')
