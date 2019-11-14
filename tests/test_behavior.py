import unittest
from design_pattern.iterator import CapitalIterator
from design_pattern.observer import Inventory,ConsoleObserver
from design_pattern.observer2 import Publisher,BinaryObserver,HexObserver

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

#todo
class Observer2Case(unittest.TestCase):
    def test_observe2(self):
        publihser = Publisher()
        hex_observer = HexObserver()
        bin_observer = BinaryObserver()

        publihser.attach(hex_observer,bin_observer)

        publihser.name = 'First set'
        publihser.value = '1'
        publihser.value = '1.0'



# if __name__ == '__main__':
#     unittest.main()
# or in cmd
# python -m unittest -v tests/test_behavior.py
