# -*- coding: utf-8 -*-
"""
Provides a way to encapsulate a group of individual factories.
"""
import abc


class Animal(abc.ABC):

    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def speak(self):
        return NotImplemented

    @abc.abstractmethod
    def act(self):
        return NotImplemented


class Dog(Animal):
    pass


class Cat(Animal):
    pass
