import unittest
from SquirrelAndEmeralds import squirrel
from random import randint
from math import factorial

class SquirelTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(squirrel(1), 1)
        self.assertEqual(squirrel(4), 2)
        self.assertEqual(squirrel(10), 3)

    def test_border(self):
        self.assertEqual(squirrel(1000), 4)
        self.assertEqual(squirrel(0), 1)

    def test_random(self):
        for i in range(10000):
            random_num = randint(0, 1000)
            self.assertEqual(squirrel(random_num), int(str(factorial(random_num))[0]))

if __name__ == "__main__":
    unittest.main()
