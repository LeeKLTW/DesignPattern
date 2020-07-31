# -*- coding: utf-8 -*-

class GraphicObjedt:
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = 'Group'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicObjedt):
    @property
    def name(self):
        return 'Circle'


class Square(GraphicObjedt):
    @property
    def name(self):
        return 'Square'


if __name__ == "__main__":
    drawing = GraphicObjedt()
    drawing.name = "My Drawing"
    drawing.children.append(Square('Red'))
    drawing.children.append(Square('Yellow'))
    print(drawing)

    group = GraphicObjedt()
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))
    drawing.children.append(group)

    print(drawing)