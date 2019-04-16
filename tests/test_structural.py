# encoding: utf-8
import unittest
from decorator import add,add_,sub,sub_

class StructureTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2,3), 6)

    def test_sub(self):
        self.assertEqual(sub(100,20), 80)

    def test_add_(self):
        self.assertEqual(add_(1,2,3), 6)

    def test_sub_(self):
        self.assertEqual(sub_(100,20), 80)

# if __name__ == '__main__':
#     unittest.main()
# or in cmd
# python -m unittest -v tests/test_structural.py