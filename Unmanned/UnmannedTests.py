import unittest
import random

from Unmanned import Unmanned

class UnmannedTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(Unmanned(10, 2, [[3, 5, 5], [5, 2, 2]]), 12)

    def test_empty(self):
        self.assertEqual(Unmanned(10, 0, []), 10)

    def test_border(self):
        self.assertEqual(Unmanned(10, 1, [[0, 100, 1]]), 110)

if __name__ == '__main__':
    unittest.main()
