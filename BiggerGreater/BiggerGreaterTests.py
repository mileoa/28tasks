import unittest
import random

from BiggerGreater import BiggerGreater

class BiggerGreaterTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(BiggerGreater("ая"), "яа")
        self.assertEqual(BiggerGreater("fff"), "")
        self.assertEqual(BiggerGreater("яаа"), "")
        self.assertEqual(BiggerGreater("аяб"), "бая")
        self.assertEqual(BiggerGreater("нклм"), "нкмл")
        self.assertEqual(BiggerGreater("вибк"), "викб")
        self.assertEqual(BiggerGreater("вкиб"), "ибвк")

    def test_border(self):
        pass

if __name__ == '__main__':
    unittest.main()
