# -*- coding: utf-8 -*-
import os


class MVCmd:
    "cmd move file with undo"

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self.rename(self.src, self.dest)
        # We can do it in just call rename(), but with decoupling into command pattern, we can use undo().

    def undo(self):
        self.rename(self.dest, self.src)

    def rename(self, src, dest):  # not self.src, self.dest, since we want to call undo()
        os.rename(src, dest)
        print(f'rename/move {src} to {dest}')


# todo testing
def main(src, dest,undo=False):
    mv = MVCmd(src,dest)

    if undo:
        mv.undo()
    else:
        mv.execute()


# todo testing
if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("src")
    parser.add_argument("dest")
    parser.add_argument("-u",action="store_true", dest='undo')
    args, unparsed = parser.parse_known_args()
