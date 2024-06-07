import unittest
import random

from ConquestCampaign import conquer_surrounding_cells

class ConquerSurroundingCellsTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(conquer_surrounding_cells([
                                                [False, False, False, False],
                                                [False, True, False, False],
                                                [False, False, False, True]
                                                    ]
                        ),
                        [
                         [False, True, False, False],
                         [True, True, True, True],
                         [False, True, True, True]
                        ]
                        )

    def test_border(self):
        self.assertEqual(conquer_surrounding_cells([[True, False, False]]),
                         [[True, True, False]])

if __name__ == '__main__':
    unittest.main()