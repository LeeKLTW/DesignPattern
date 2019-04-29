# -*- coding: utf-8 -*-
"""
An operating system using a multi-server approach, similar to MINIX 3 GNU Hurd.
A multiserver operating system has a minimal kernel, called the microkernel.

The pros of this approach are that the operating system can become more fault-tolerant, reliable, and secure.

The cons of this approach are the performance overhead and the complexity of system programming,
because the message passing is more complex than the shared memory model used in monolithic kernels such as Linux.
"""

from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State','new running sleeping restart zombie') #<enum 'State'>
# [<State.new: 1>, <State.running: 2>, <State.sleeping: 3>, <State.restart: 4>, <State.zombie: 5>]
# 'name', 'value'

class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        return NotImplemented

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        return NotImplemented

    @abstractmethod
    def kill(self, restart=True):
        return NotImplemented

class FileServer(Server):
    def __init__(self):
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print(f'Booting {self}')
        self.state = State.running

    def kill(self,restart=True):
        print(f'Killing {self}')
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permission):
        print(f'trying to create the file {name} for {user} with permission {permission}')


class ProcessServer(Server):

    def boot(self):
        pass

    def kill(self):
        pass


class OperatingSystem:
    """The Facade"""
    pass