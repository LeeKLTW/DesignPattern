# -*- coding: utf-8 -*-
# reference: https://github.com/faif/python-patterns/blob/master/patterns/creational/pool.py

class ObjectPool:
    def __init__(self, queue_, auto_get=False):
        self._queue = queue_
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

def main():
    import queue

    def test_object(queue):
        pool = ObjectPool(queue, True)
        print(f"Inside func: {pool.item}")

    sample_queue = queue.Queue()
    sample_queue.put("yam")

    with ObjectPool(sample_queue) as obj:
        print(f"Inside func with: {obj}")
    # Inside func with: yam

    print(f"Outside with: {sample_queue.get()}")
    # Outside with: yam

    sample_queue.put("sam")

    test_object(sample_queue)
    # Inside func: sam

    if not sample_queue.empty():
        print(sample_queue.get())
    # sam

if __name__ == "__main__":
    main()