import unittest
import random

from TankRush import TankRush

class TankRushTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "34 98"), True)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "45 86"), False)

    def test_border(self):
        self.assertEqual(TankRush(1, 1, "1", 1, 1, "1"), True)
        self.assertEqual(TankRush(1, 1, "1", 1, 1, "2"), False)
        self.assertEqual(TankRush(1, 1, "1", 1, 2, "12"), False)
        self.assertEqual(TankRush(1, 2, "12", 1, 1, "1"), True)

if __name__ == '__main__':
    unittest.main()
