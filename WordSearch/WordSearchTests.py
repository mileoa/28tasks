import unittest
import random

from WordSearch import WordSearch

class WordSearchTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(WordSearch(12,
                                    "1) строка разбивается на набор строк через выравнивание по заданной ширине.",
                                    "строк"),
                        [0, 0, 0, 1, 0, 0, 0]
                                    )
        self.assertEqual(WordSearch(5,
                                    "Эта строка не попадёт.", 
                                    "строка"
                                    ),
                        [0, 0, 0, 0, 0]
                        )
        self.assertEqual(WordSearch(5,
                                    "Эта строка не попадёт.", 
                                    "строк"
                                    ),
                        [0, 1, 0, 0, 0]
                        )

    def test_random(self):
        pass

    def test_border(self):
        self.assertEqual(WordSearch(1, "g h", "g"), [1, 0])
        self.assertEqual(WordSearch(4, "abc", "abc"), [1])

if __name__ == '__main__':
    unittest.main()