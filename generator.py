# encoding: utf-8

def bizzbuzz(start, end, step):
    for i in range(start, end, step):
        if i % 6 == 0:
            yield 'bizzbuzz'
        elif i % 2 == 0:
            yield 'bizz'
        elif i % 3 == 0:
            yield 'buzz'
        else:
            yield i

generator = bizzbuzz(0,18,1)

for i in generator:
    print(next(generator))
