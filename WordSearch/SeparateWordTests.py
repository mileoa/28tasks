import unittest
import random

from WordSearch import separate_word
class SeparateWordTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(separate_word("hello!", 2), ["he", "ll", "o!"])
        self.assertEqual(separate_word("hello", 2), ["he", "ll", "o"])
        self.assertEqual(separate_word("hello", 7), ["hello"])

if __name__ == '__main__':
    unittest.main()