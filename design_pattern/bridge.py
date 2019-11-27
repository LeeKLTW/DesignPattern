# -*- coding: utf-8 -*-
"""
Sharing similarities with the adapter pattern,
the bridge pattern is different from it,
in the sense that it is used up-front to define an abstraction and
its implementation in a decoupled way so that both can vary independently.
"""


# ConcreteImplementor
class DrawingAPI1:
    def draw_circle(self, x, y, radius):
        print(f'API1.circle at {x}:{y} radius {radius}')


# ConcreteImplementor
class DrawingAPI2:
    def draw_circle(self, x, y, radius):
        print(f'API2.circle at {x}:{y} radius {radius}')


class CircleShape:
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, pct):
        self._radius *= pct


def main():
    shapes = (CircleShape(1, 2, 3, DrawingAPI1()), CircleShape(5, 7, 11, DrawingAPI2()))
    for shape in shapes:
        shape.draw()
        shape.scale(2.5)
        shape.draw()
        print('')
