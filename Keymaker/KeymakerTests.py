import unittest

from Keymaker import Keymaker

class KeymakerTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(Keymaker(1), "1")
        self.assertEqual(Keymaker(2), "10")
        self.assertEqual(Keymaker(3), "100")
        self.assertEqual(Keymaker(4), "1001")
        self.assertEqual(Keymaker(5), "10010")
        self.assertEqual(Keymaker(6), "100100")

if __name__ == '__main__':
    unittest.main()
