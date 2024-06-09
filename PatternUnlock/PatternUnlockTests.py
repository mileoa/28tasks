import unittest
import random

from PatternUnlock import PatternUnlock

class PatternUnlockTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]), "982843")
        self.assertEqual(PatternUnlock(11, [1, 2, 3, 4, 5, 6, 1, 9, 8, 7, 2]), "141421")

    def test_border(self):
        self.assertEqual(PatternUnlock(2, [1, 2]), "1")
        self.assertEqual(PatternUnlock(2, [1, 8]), "141421")

if __name__ == '__main__':
    unittest.main()
