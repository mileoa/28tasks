import unittest
import random

from TreeOfLife import TreeOfLife

class TreeOfLifeTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TreeOfLife(3,4, 12, [
                                                ".+..",
                                                "..+.",
                                                ".+.."
                                             ]
                                    ),
                        [
                            ".+..",
                            "..+.",
                            ".+.."
                        ]
                        )

    def test_border(self):
        self.assertEqual(TreeOfLife(3, 4, 1, [".+..","..+.",".+.."]), ["++++","++++","++++"])
        self.assertEqual(TreeOfLife(3, 4, 0, [".+..","..+.",".+.."]), [".+..","..+.",".+.."])

        self.assertEqual(TreeOfLife(3, 1, 2, [".", "+", "."]), [".", ".", "."])
        self.assertEqual(TreeOfLife(3, 1, 3, [".", "+", "."]), ["+", "+", "+"])
        self.assertEqual(TreeOfLife(1, 3, 2, [".+."]), ["..."])
        self.assertEqual(TreeOfLife(1, 3, 3, [".+."]), ["+++"])

        self.assertEqual(TreeOfLife(1, 1, 5, ["+"]), ["+"])
        self.assertEqual(TreeOfLife(1, 1, 1, ["."]), ["+"])

        self.assertEqual(TreeOfLife(1, 4, 2, [".++."]), ["...."])

if __name__ == '__main__':
    unittest.main()
