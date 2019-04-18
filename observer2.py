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
            print(f'{type(self).__name__} with error: {e}')
        else:
            self.notify()

    def attach(self,*observers):
        for observer in observers:
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

class Observer:
    def __init__(self):
        self.name = None
        self.value = None

    def __str__(self):
        return f'{type(self).__name__} receive {self.name} with {self.value}'

    def receive(self, publisher):
        pass


class HexObserver(Observer):
    def receive(self, publisher):
        self.name = publisher.name
        self.value = hex(publisher.value)
        print(self)


class BinaryObserver(Observer):
    def receive(self, publisher):
        self.name = publisher.name
        self.value = bin(publisher.value)
        print(self)
