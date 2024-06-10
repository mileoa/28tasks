import unittest
import random

from SumOfThe import SumOfThe

class SumOfTheTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(SumOfThe(5, [10, -25, -45, -35, 5]), -45)
        self.assertEqual(SumOfThe(2, [-45, -45]), -45)

if __name__ == '__main__':
    unittest.main()
