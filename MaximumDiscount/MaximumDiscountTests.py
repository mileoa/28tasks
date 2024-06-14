import unittest
import random

from MaximumDiscount import MaximumDiscount

class MaximumDiscountTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(MaximumDiscount(7, [100, 350, 200, 300, 250, 400, 150]), 450)
        self.assertEqual(MaximumDiscount(1, [100]), 0)
        self.assertEqual(MaximumDiscount(2, [100, 200]), 0)
        self.assertEqual(MaximumDiscount(3, [100, 200, 300]), 100)
        self.assertEqual(MaximumDiscount(4, [100, 200, 300, 50]), 100)
        self.assertEqual(MaximumDiscount(5, [100, 200, 300, 50, 20]), 100)

    def test_empty(self):
        self.assertEqual(MaximumDiscount(0, []), 0)

if __name__ == '__main__':
    unittest.main()
