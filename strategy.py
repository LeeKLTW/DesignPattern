# -*- coding: utf-8 -*-
"""
Because Python has first-class functions, the strategy pattern is unnecessary.
Knowing the pattern exists can still help us choose a correct design for our program,
but implement it using a more readable syntax.
"""
import abc
import os
from typing import overload,runtime

from PIL import Image
from argparse import ArgumentParser

parser = ArgumentParser()

"""
To see why strategy pattern is unnecessary, see function way.
"""


def tiled_strategy(img_file, desktop_size):
    pass


def centered_strategy(img_file, desktop_size):
    pass


def scaled_strategy(img_file, desktop_size):
    pass


"""
However, it will be useful to use class for abc.
"""


class Strategy:
    @abc.abstractmethod
    def __call__(self, img_file, desktop_size):
        return NotImplemented

    @abc.abstractmethod
    def __str__(self):
        return NotImplemented


class TiledStrategy(Strategy):
    def __call__(self, img_file, desktop_size):
        in_img = Image.open(fp=img_file)
        out_img = Image.new(mode="RGB", size=desktop_size)
        num_tiles = [o // i + 1 for o, i in zip(out_img.size, in_img.size)]
        for x in range(num_tiles[0]):
            for y in range(num_tiles[1]):
                out_img.paste(im=in_img, box=(
                    in_img.size[0] * x, in_img.size[1] * y, in_img.size[0] * (x + 1), in_img.size[1] * (y + 1)))
        return out_img

    def __str__(self):
        return 'tiled'


class CenteredStrategy(Strategy):
    def __call__(self, img_file, desktop_size):
        in_img = Image.open(fp=img_file)
        out_img = Image.new(mode="RGB", size=desktop_size)
        left = (out_img.size[0] - in_img.size[0]) // 2
        top = (out_img.size[1] - in_img.size[1]) // 2
        out_img.paste(im=in_img, box=(left, top, left + in_img.size[0], top + in_img.size[1]),
                      )
        return out_img

    def __str__(self):
        return 'centered'


class ScaledStrategy(Strategy):
    def __call__(self, img_file, desktop_size):
        in_img = Image.open(fp=img_file)
        out_img = in_img.resize(desktop_size)
        return out_img

    def __str__(self):
        return 'scaled'


def main(in_img_path, desktop_size, tiled, centered, scaled):
    if not os.path.exists(in_img_path):
        print('File does not exist')
        return
    elif tiled + centered + scaled < 1:
        print('Please select a strategy.')
        return
    elif tiled + centered + scaled > 1:
        print('Please select ONLY ONE strategy.')

    elif tiled:
        strategy = TiledStrategy()
        out_img = strategy(in_img_path, desktop_size)

    elif centered:
        strategy = CenteredStrategy()
        out_img = strategy(in_img_path, desktop_size)

    elif scaled:
        strategy = ScaledStrategy()
        out_img = strategy(in_img_path, desktop_size)

    out_img_path = os.path.splitext(in_img_path)[0] + f'_{strategy}' + os.path.splitext(in_img_path)[1]
    out_img.save(out_img_path)

if __name__ == '__main__':
    parser.add_argument("in_img_path", type=str)
    parser.add_argument("-x", dest="x", type=int)
    parser.add_argument("-y", dest="y", type=int)
    parser.add_argument("-t", dest="tiled", action="store_true")
    parser.add_argument("-c", dest="centered", action="store_true")
    parser.add_argument("-s", dest="scaled", action="store_true")

    args, unparsed = parser.parse_known_args()
    desktop_size = (args.x, args.y)
    main(args.in_img_path, desktop_size, args.tiled, args.centered, args.scaled)
