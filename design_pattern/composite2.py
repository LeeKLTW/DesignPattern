# -*- coding: utf-8 -*-
# neural network

from abc import ABC
from collections.abc import Iterable

class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return

        for s in self: # Iterable
            for o in other: # Iterable
                s.outputs.append(o)
                o.inputs.append(s)

class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __iter__(self):
        yield self

    def __str__(self):
        return f"{self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs"

class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super(NeuronLayer, self).__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f"{name}-{x}"))

    def __str__(self):
        return f"{self.name} with {len(self)} neurons"

# TODO: example