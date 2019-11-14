# -*- coding: utf-8 -*-

"""
__iter__
__next__
"""

def bizzbuzz(start, end, step):
    """

    Args:
        start:
        end:
        step:

    Returns:

    >>> [i for i in bizzbuzz(0,18,1)]
    ['bizzbuzz', 1, 'bizz', 'buzz', 'bizz', 5, 'bizzbuzz', 7, 'bizz', 'buzz', 'bizz', 11, 'bizzbuzz', 13, 'bizz', 'buzz', 'bizz', 17]

    """
    for i in range(start, end, step):
        if (i % 2 == 0) and (i % 3 == 0):
            yield 'bizzbuzz'
        elif i % 2 == 0:
            yield 'bizz'
        elif i % 3 == 0:
            yield 'buzz'
        else:
            yield i
