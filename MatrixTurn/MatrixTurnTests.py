import unittest

from MatrixTurn import MatrixTurn

class MatrixTurnTests(unittest.TestCase):

    def test_regression(self):
        Matrix: list[str] = ["123456", "234567", "345678", "456789"]
        MatrixTurn(Matrix, 4, 6, 3)
        self.assertEqual(Matrix,
                        ["432123", "565434", "676545", "789876"])
        
        Matrix = ["1234", "2345", "3456", "4567", "5678", "6789"]
        MatrixTurn(Matrix, 6, 4, 1)
        self.assertEqual(Matrix,
                        ["2123", "3434", "4545", "5656", "6767", "7898"])

    def test_border(self):
        Matrix: list[str] = ["12", "43"]
        MatrixTurn(Matrix, 2, 2, 1)
        self.assertEqual(Matrix, ["41", "32"])

        Matrix = ["12", "43"]
        MatrixTurn(Matrix, 2, 2, 2)
        self.assertEqual(Matrix, ["34", "21"])

        Matrix = ["12", "43"]
        MatrixTurn(Matrix, 2, 2, 3)
        self.assertEqual(Matrix, ["23", "14"])

        Matrix = ["12", "43"]
        MatrixTurn(Matrix, 2, 2, 4)
        self.assertEqual(Matrix, ["12", "43"])


if __name__ == '__main__':
    unittest.main()
