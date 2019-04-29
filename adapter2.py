# -*- coding: utf-8 -*-
class Club:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the club {self.name}'

    def organize_event(self):
        return f'hires an artist to perform for the people.'


class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the musician {self.name}'

    def play(self):
        return 'play music'


class Dancer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the dancer {self.name}'

    def dance(self):
        return 'does a dance performance'

class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Club('Bossa Nova'), Musician('Astrud Gilberto'), Dancer('Kevin Goldschmitt')]
    for obj in objects:
        if hasattr(obj,'play'):
            adapted_methods = dict(organized_event=obj.play)
            obj = Adapter(obj, adapted_methods)
            print(f'{obj} {obj.organized_event()}')

        elif hasattr(obj,'dance'):
            adapted_methods = dict(organized_event=obj.dance)
            obj = Adapter(obj, adapted_methods)
            print(f'{obj} {obj.organized_event()}')

# todo club part

