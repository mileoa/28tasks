import unittest

from BigMinus import BigMinus

class BigMinusTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(BigMinus("1234567891", "1"), "1234567890")
        self.assertEqual(BigMinus("1", "321"), "320")
        self.assertEqual(BigMinus("61", "321"), "260")
        self.assertEqual(BigMinus("1234567890", "1234567890"), "0")
        self.assertEqual(BigMinus("110", "100"), "10")

    def test_border(self):
        self.assertEqual(BigMinus("0", "321"), "321")
        self.assertEqual(BigMinus("321", "0"), "321")
        self.assertEqual(BigMinus("0", "0"), "0")

if __name__ == '__main__':
    unittest.main()
