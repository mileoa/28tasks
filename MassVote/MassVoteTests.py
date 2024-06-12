import unittest
import random

from MassVote import MassVote

class MassVoteTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(MassVote(5, [60, 10, 10, 15, 5]), "majority winner 1")
        self.assertEqual(MassVote(3, [10, 15, 10]), "minority winner 2")
        self.assertEqual(MassVote(4, [111, 111, 110, 110]), "no winner")
        self.assertEqual(MassVote(3, [112, 333, 334]), "minority winner 3")
        self.assertEqual(MassVote(3, [100, 6172788, 6172790]), "no winner")

    def test_border(self):
        self.assertEqual(MassVote(1, [111]), "majority winner 1")

if __name__ == '__main__':
    unittest.main()
