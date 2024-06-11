import unittest
import random

from TheRabbitsFoot import make_encode_matrix

class MakeMatrixTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(make_encode_matrix("отдаймоюкроличьюлапку"),
                         [
                            ["о", "т", "д", "а", "й"],
                            ["м", "о", "ю", "к", "р"],
                            ["о", "л", "и", "ч", "ь"],
                            ["ю", "л", "а", "п", "к"],
                            ["у", " ", " ", " ", " "]
                         ])

    def test_border(self):
        self.assertEqual(make_encode_matrix("a b"), [["a", " "], ["b", " "]])

if __name__ == '__main__':
    unittest.main()