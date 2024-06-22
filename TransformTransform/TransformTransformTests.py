import unittest
import random

from TransformTransform import TransformTransform

class TransformTransformTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TransformTransform([1], 1), False)
        self.assertEqual(TransformTransform([2], 1), True)
        self.assertEqual(TransformTransform([1, 2], 2), False)


    def test_border(self):
        self.assertEqual(TransformTransform([1, 2, 3, 4, 5, 6, 7, 2, 3, 1, 2, 3, 4, 5, 6, 7, 1, 3, 5, 6, 6, 2, 1], 23), False)

if __name__ == '__main__':
    unittest.main()
