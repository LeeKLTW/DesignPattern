# -*- coding: utf-8 -*-
"""
Because Python has first-class functions, the strategy pattern is unnecessary.
Knowing the pattern exists can still help us choose a correct design for our program,
but implement it using a more readable syntax.
"""
from PIL import Image


class TiledStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = Image.open(fp=img_file)
        out_img = Image.new(model="RGB", size=desktop_size)
        num_tiles = [o // i + 1 for o, i in zip(in_img.size, out_img.size)]
        for x in range(num_tiles[0]):
            for y in range(num_tiles[1]):
                out_img.paste(im=in_img, box=(
                in_img.size[0] * x, in_img.size[1] * y, in_img.size[0] * (x + 1), in_img.size[1] * (y + 1)))
        return out_img


class CenteredStrategy:
    def make_background(self, img_file, desktop_size):
        pass


class ScaledStrategy:
    def make_background(self, img_file, desktop_size):
        pass
