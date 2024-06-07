import unittest
import random

from ConquestCampaign import generate_polygon

class GeneratePolygonTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(generate_polygon(3, 4), [[False, False, False, False],
                                                  [False, False, False, False],
                                                  [False, False, False, False]])
        self.assertEqual(generate_polygon(1, 1), [[False]])

if __name__ == '__main__':
    unittest.main()