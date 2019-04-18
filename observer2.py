# -*- coding: utf-8 -*-
class Publisher:
    def __init__(self):
        self.observers = []
        self._name = None
        self._value = 0

    def __str__(self):
        return f"{type(self).__name__} {self._name} {self._value}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        try:
            self._name = str(value)
        except ValueError as e:
            print(e)
        else:
            self.notify()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            self._value = int(value)
        except ValueError as e:
            print(e)
        else:
            self.notify()

    def attach(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print(f'{observer} already attached')

    def detach(self,observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print(f'{observer} not in attached list.')

    def notify(self):
        [observer.receive(self) for observer in self.observers]


class HexObserver:
    def receive(self, publisher):
        name = publisher.name
        value = hex(publisher.value)
        print(f'{type(self).__name__} receive {name} with {value}')

class BinaryObserver:
    def receive(self, publisher):
        name = publisher.name
        value = bin(publisher.value)
        print(f'{type(self).__name__} receive {name} with {value}')
