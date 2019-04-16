# encoding: utf-8
class CapitalIterator:
    def __init__(self,string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self

iterator = CapitalIterator('The quick brown fox jump over the lazy dog.')

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

