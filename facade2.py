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

State = Enum('State', 'new running sleeping restart zombie')  # <enum 'State'>


# [<State.new: 1>, <State.running: 2>, <State.sleeping: 3>, <State.restart: 4>, <State.zombie: 5>]
# 'name', 'value'

class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    def boot(self):
        print(f'Booting {self}')
        self.state = State.running

    def kill(self, restart=True):
        if restart:
            self.state = State.restart
            print(f'Restart {self}')
        else:
            self.state =  State.zombie
            print(f'Killing {self}')


class FileServer(Server):
    def __init__(self):
        self.name = 'FileServer'
        self.state = State.new

    def create_file(self, user, name, permission):
        print(f'trying to create the file {name} for {user} with permission {permission}')


class ProcessServer(Server):
    def __init__(self):
        self.name = 'ProcessServer'
        self.state = State.new

    def create_process(self, user, name):
        print(f'tring to create process {name} for {user}')


class User:
    pass


class File:
    pass


class Process:
    pass


class OperatingSystem:
    """The Facade"""

    def __init__(self):
        self.file_server = FileServer()
        self.process_server = ProcessServer()

    def start(self):
        [i.boot() for i in (self.file_server, self.process_server)]

    def create_file(self, user, name, permissions):
        return self.file_server.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.process_server.create_process(user, name)

    def restart(self):
        [i.kill() for i in (self.file_server, self.process_server)]

    def shutdown(self):
        [i.kill(restart=False) for i in (self.file_server, self.process_server)]


def main():
    os = OperatingSystem()
    os.start()
    os.create_file('root', 'tmp/log', '-rw-r-r')
    os.create_process('root', 'bin')
    os.restart()
    os.shutdown()
    print('Finish. Shutdown')


if __name__ == '__main__':
    main()
