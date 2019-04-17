import unittest
from iterator import CapitalIterator
from observer import Inventory,ConsoleObserver

class IteratorCase(unittest.TestCase):
    def test_iterator(self):
        iterator = CapitalIterator('The quick brown fox jump over the lazy dog.')

        self.assertEqual(next(iterator), 'The')
        self.assertEqual(next(iterator), 'Quick')
        self.assertEqual(next(iterator), 'Brown')
        self.assertEqual(next(iterator), 'Fox')
        self.assertEqual(next(iterator), 'Jump')
        self.assertEqual(next(iterator), 'Over')
        self.assertEqual(next(iterator), 'The')
        self.assertEqual(next(iterator), 'Lazy')
        self.assertEqual(next(iterator), 'Dog.')

class ObserverCase(unittest.TestCase):
    def test_observe(self):
        inv = Inventory()
        console = ConsoleObserver(inv)
        inv.attach(console)

        inv.product = "Widget"
        inv.quantity = 5

        self.assertEqual(inv.product,console.inventory.product)
        self.assertEqual(inv.quantity,console.inventory.quantity)


# if __name__ == '__main__':
#     unittest.main()
# or in cmd
# python -m unittest -v tests/test_behavior.py
