import unittest
import random

from LineAnalysis import LineAnalysis

class LineAnalysisTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(LineAnalysis("*..*..*..*..*..*..*"), True)
        self.assertEqual(LineAnalysis("*..*...*..*..*..*..*"), False)
        self.assertEqual(LineAnalysis("*..*..*..*..*..**..*"), False)
        self.assertEqual(LineAnalysis("*.......*.......*"), True)
        self.assertEqual(LineAnalysis("*.......*......*"), False)

    def test_border(self):
        self.assertEqual(LineAnalysis("*"), True)
        self.assertEqual(LineAnalysis("***"), True)
        self.assertEqual(LineAnalysis("**"), True)
        self.assertEqual(LineAnalysis("*.*"), True)

if __name__ == '__main__':
    unittest.main()
