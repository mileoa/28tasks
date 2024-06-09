import unittest
import random

from MadMax import MadMax

class MadMaxTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(MadMax(7, [1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 7, 6, 5, 4])
        self.assertEqual(MadMax(7, [3, 7, 5, 4, 2, 6, 1]), [1, 2, 3, 7, 6, 5, 4])

    def test_random(self):
        pass

    def test_border(self):
        self.assertEqual(MadMax(1, [1]), [1])

if __name__ == '__main__':
    unittest.main()