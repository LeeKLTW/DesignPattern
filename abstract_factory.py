# -*- coding: utf-8 -*-
"""
Provides a way to encapsulate a group of individual factories.
"""
import abc


class Animal(abc.ABC):

    def __repr__(self):
        pass

    @abc.abstractmethod
    def speak(self):
        return NotImplemented

    @abc.abstractmethod
    def act(self):
        return NotImplemented


class Dog(Animal):
    def __repr__(self):
        return f'Dog at {id(self)}'

    def speak(self):
        return 'woof'

    def act(self):
        return 'running'


class Cat(Animal):
    def __repr__(self):
        return f'Cat at {id(self)}'

    def speak(self):
        return 'meow'

    def act(self):
        return 'climbing'
