import unittest
import random

from SherlockValidString import SherlockValidString

class SherlockValidStringTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(SherlockValidString("xyz"), True)
        self.assertEqual(SherlockValidString("xyzaa"), True)
        self.assertEqual(SherlockValidString("xxyyz"), True)
        self.assertEqual(SherlockValidString("xyzzz"), False)
        self.assertEqual(SherlockValidString("xxyyza"), False)
        self.assertEqual(SherlockValidString("xxyyzabc"), False)

    def test_border(self):
        self.assertEqual(SherlockValidString("aa"), True)
        self.assertEqual(SherlockValidString("ab"), True)

if __name__ == '__main__':
    unittest.main()
