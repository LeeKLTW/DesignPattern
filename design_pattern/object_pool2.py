# -*- coding: utf-8 -*-
# Reference: https://sourcemaking.com/design_patterns/object_pool/python/1

class ReusablePool:
    def __init__(self, size):
        self._reusables = [Reusable() for _ in range(size)]

    # TODO: implement instantiates new objects as they are empty
    def acquire(self):
        print("get a reusable from pool")
        return self._reusables.pop()

    # TODO: implement a facility to clean up unused
    def release(self, reusable):
        print("give a reusable to pool")
        self._reusables.append(reusable)

class Reusable:
    def __repr__(self):
        return f"<Reusable at {hex(id(self))}>"


def main():
    reusable_pool = ReusablePool(10)
    reusable = reusable_pool.acquire()
    print(f"Pool with size {len(reusable_pool._reusables)} with {reusable_pool._reusables}")
    reusable_pool.release(reusable)
    print(f"Pool with size {len(reusable_pool._reusables)} with {reusable_pool._reusables}")

if __name__ == "__main__":
    main()