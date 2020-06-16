# -*- coding: utf-8 -*-
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