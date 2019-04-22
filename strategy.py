# -*- coding: utf-8 -*-
"""
Because Python has first-class functions, the strategy pattern is unnecessary.
Knowing the pattern exists can still help us choose a correct design for our program,
but implement it using a more readable syntax.
"""
from PIL import Image

class TiledStrategy:
    def make_background(self,img_file, desktop_size):
        pass

class CenteredStrategy:
    def make_background(self,img_file, desktop_size):
        pass

class ScaledStrategy:
    def make_background(self,img_file, desktop_size):
        pass
