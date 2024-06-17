import unittest
import random

from ShopOLAP import ShopOLAP

class ShopOLAPTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(ShopOLAP(5, [
                                        "платье1 5",
                                        "сумка32 2",
                                        "платье1 1",
                                        "сумка23 2",
                                        "сумка128 4"
                                     ]
                        ),
                        [
                            "платье1 6",
                            "сумка128 4",
                            "сумка23 2",
                            "сумка32 2"
                        ]
        )
        self.assertEqual(ShopOLAP(2, ["abc 3", "aba 3"]), ["aba 3", "abc 3"])
        self.assertEqual(ShopOLAP(3, ["abc 4", "abd 3", "aba 4"]), ["aba 4", "abc 4", "abd 3"])

    def test_border(self):
        self.assertEqual(ShopOLAP(1, ["платье1 10"]), ["платье1 10"])
        self.assertEqual(ShopOLAP(2, ["платье1 10", "платье1 11"]), ["платье1 21"])

if __name__ == '__main__':
    unittest.main()