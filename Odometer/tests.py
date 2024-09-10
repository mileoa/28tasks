import unittest
import random

from odometer import odometer


class OdometerTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(odometer([10, 1, 20, 2]), 30)
        self.assertEqual(odometer([10, 1, 20, 4]), 70)
        self.assertEqual(odometer([10, 1, 20, 4, 10, 7]), 100)


if __name__ == "__main__":
    unittest.main()
