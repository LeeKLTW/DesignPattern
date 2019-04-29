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

State = Enum('State','new running sleeping restart zombie')

class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass

class FileServer(Server):
    pass

class ProcessServer(Server):
    pass

class OperatingSystem:
    """The Facade"""
    pass