# -*- coding: utf-8 -*-
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    
class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size,color):
        for p in products:
            if p.size == size and p.color == color:
                yield p




class Specification:
    def is_satisfied(self, item):
        pass

class Filter:
    def filter(self, item, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

print("Green product products (old):")
pf = ProductFilter()
for p in pf.filter_by_color(products,Color.GREEN):
    print(f" - {p.name} is green")

print("Green product products (new):")
bf = BetterFilter()
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products,green):
    print(f" - {p.name} is green")

print("Large and blue items (old):")
pf = ProductFilter()
for p in pf.filter_by_size_and_color(products,Size.LARGE, Color.BLUE):
    print(f" - {p.name} is large and blue")

print("Large and blue items (new):")
bf = BetterFilter()
large_blue = AndSpecification(SizeSpecification(Size.LARGE), ColorSpecification(Color.BLUE))
for p in bf.filter(products, large_blue):
    print(f" - {p.name} is large and blue")