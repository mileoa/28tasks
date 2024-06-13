import unittest
import random

from UFO import UFO

class UFOTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(UFO(2, [1234, 1777], True), [668, 1023])
        self.assertEqual(UFO(2, [1234, 1777], False), [4660, 6007])
        self.assertEqual(UFO(1, [10], True), [8])
        self.assertEqual(UFO(1, [10], False), [16])

    def test_empty(self):
        self.assertEqual(UFO(0, [], True), [])
        self.assertEqual(UFO(0, [], False), [])

    def test_random(self):
        pass

    def test_border(self):
        self.assertEqual(UFO(1, [0], True), [0])
        self.assertEqual(UFO(1, [0], False), [0])
        self.assertEqual(UFO(1, [1], True), [1])
        self.assertEqual(UFO(1, [1], False), [1])

if __name__ == '__main__':
    unittest.main()
