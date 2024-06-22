import unittest

from Football import Football

class FootballTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(Football([1, 3, 2], 3), True)
        self.assertEqual(Football([3, 2, 1], 3), True)
        self.assertEqual(Football([1, 7, 5, 3, 9], 5), True)
        self.assertEqual(Football([9, 5, 3, 7, 1], 5), False)
        self.assertEqual(Football([1, 4, 3, 2, 5], 5), True)

    def test_border(self):
        self.assertEqual(Football([1], 1), True)
        self.assertEqual(Football([1, 2], 2), True)
        self.assertEqual(Football([2, 1], 2), True)

if __name__ == '__main__':
    unittest.main()
