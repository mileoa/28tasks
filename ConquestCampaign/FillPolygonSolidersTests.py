import unittest
import random

from ConquestCampaign import fill_polygon_soliders

class FillPolygonSolidersTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(fill_polygon_soliders([[False, False, False, False],
                                                  [False, False, False, False],
                                                  [False, False, False, False]],
                                                  2, [2,2, 3,4]),
                        [
                         [False, False, False, False],
                         [False, True, False, False],
                         [False, False, False, True]
                        ]
                        )


    def test_border(self):
        self.assertEqual(fill_polygon_soliders([[False]], 1, [1, 1]), [[True]])

if __name__ == '__main__':
    unittest.main()