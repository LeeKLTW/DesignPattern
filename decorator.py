# encoding: utf-8
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
    return sum(args)


@decorator_function
def sub(x, y):
    return x - y


add(1, 2, 3, 4)
add(2, 2, 3, 4)
sub(10, 2)


class decorator_class:
    def __init__(self, fn):
        self.fn = fn

    @wraps(self.fn)
    def __call__(self, *args, **kwargs):  # similar to decorator function but use __call__, and add instance self
        t_start = time.time()
        result = self.fn(*args, **kwargs)
        t_cost = time.time() - t_start
        logging.debug('Recorded by class.')
        logging.info(f'Function {fn.__name__} with Arguments: {args}, {kwargs} time cost{t_cost}')
        return result


@decorator_class
def add(*args):
    return sum(args)


@decorator_class
def sub(x, y):
    return x - y


add(1, 2, 3, 4)
add(2, 2, 3, 4)
sub(8, 2)
