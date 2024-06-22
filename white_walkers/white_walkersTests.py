import unittest

from white_walkers import white_walkers

class white_walkersTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(white_walkers("axxb6===4xaf5===eee5"), True)
        self.assertEqual(white_walkers("5==ooooooo=5=5"), False)
        self.assertEqual(white_walkers("abc=7==hdjs=3gg1=======5"), True)
        self.assertEqual(white_walkers("aaS=8"), False)
        self.assertEqual(white_walkers("9===1===9===1===9"), True)

    def test_empty(self):
        self.assertEqual(white_walkers(""), False)

    def test_border(self):
        self.assertEqual(white_walkers("9===1"), True)
        self.assertEqual(white_walkers("9==="), False)
        self.assertEqual(white_walkers("===9"), False)
        self.assertEqual(white_walkers("==="), False)

if __name__ == '__main__':
    unittest.main()
