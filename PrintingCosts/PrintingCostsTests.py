import unittest
import random

from PrintingCosts import PrintingCosts

class PrintingCostsTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(PrintingCosts("& iou"), 24+15+20+17)
        self.assertEqual(PrintingCosts("& iouй"), 24+15+20+17+23)

    def test_empty(self):
        self.assertEqual(PrintingCosts(""), 0)

    def test_border(self):
        self.assertEqual(PrintingCosts("&"), 24)

if __name__ == '__main__':
    unittest.main()