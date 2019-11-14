# -*- coding: utf-8 -*-
import logging
from functools import wraps
import time


logging.basicConfig(filename='decorator.log', level=logging.DEBUG, format="[%(levelname)-8s]- %(message)s")


def decorator_function(fn):
    @wraps(fn)
    def wrapper_function(*args, **kwargs):
        t_start = time.time()
        result = fn(*args, **kwargs)
        t_cost = time.time() - t_start
        logging.debug('Recorded by function.')
        logging.info(f'Function {fn.__name__} with Arguments: {args}, {kwargs} time cost{t_cost}')
        return result

    return wrapper_function


@decorator_function
def add(*args):
    """

    Args:
        *args:

    Returns:

    >>> add(1, 2, 3, 4)
    10
    >>> add(2, 2, 3)
    7

    """
    return sum(args)


@decorator_function
def sub(x, y):
    """

    Args:
        x:
        y:

    Returns:
    >>> sub(10, 2)
    8
    """
    return x - y




class decorator_class:
    def __init__(self, fn):
        self.fn = fn

    # @wraps(self.fn) # issue
    def __call__(self, *args, **kwargs):  # similar to decorator function but use __call__, and add instance self
        t_start = time.time()
        result = self.fn(*args, **kwargs)
        t_cost = time.time() - t_start
        logging.debug('Recorded by class.')
        logging.info(f'Function {self.fn.__name__} with Arguments: {args}, {kwargs} time cost{t_cost}')
        return result

@decorator_class
def add_(*args):
    """

    Args:
        *args:

    Returns:

    >>> add(1, 2, 3, 4)
    10
    >>> add(2, 2, 3)
    7


    """
    return sum(args)


@decorator_class
def sub_(x, y):
    """

    Args:
        x:
        y:

    Returns:
    >>> sub(8, 2)
    """
    return x - y


