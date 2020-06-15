# -*- coding: utf-8 -*-
from abc import ABC

class Renderer(ABC): # client-provider middleman
  def render_circle(self, radius):
    pass

class VectorRenderer(Renderer):
  def render_circle(self, radius):
    print(f"Drawing a circle of radius {radius}")

class RasterRender(Renderer):
  def render_circle(self, radius):
    print(f"Drawing pixels for circle of radius {radius}")


class Shape: # client-provider middleman
  def __init__(self, renderer):
    self.renderer = renderer
  def draw(self):pass
  def resize(self, factor):pass


class Circle(Shape):
  def __init__(self, renderer, radius):
    super().__init__(renderer)
    self.radius = radius

  def draw(self):
    self.renderer.render_circle(self.radius)

  def resize(self, factor):
    self.radius *= factor