import unittest
import random

from TheRabbitsFoot import trans_matrix

class TransMatrixTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(trans_matrix([
                            ["о", "т", "д", "а", "й"],
                            ["м", "о", "ю", "к", "р"],
                            ["о", "л", "и", "ч", "ь"],
                            ["ю", "л", "а", "п", "к"],
                            ["у", " ", " ", " ", " "]
                         ]
                         ),
                        [
                            ["о", "м", "о", "ю", "у"],
                            ["т", "о", "л", "л", " "],
                            ["д", "ю", "и", "а", " "],
                            ["а", "к", "ч", "п", " "],
                            ["й", "р", "ь", "к", " "]
                        ],
        )

    def test_border(self):
        self.assertEqual(trans_matrix([["a"]]), [["a"]])
        self.assertEqual(trans_matrix([["a", "b"]]), [["a"], ["b"]])

if __name__ == '__main__':
    unittest.main()