import unittest
import random

from SynchronizingTables import SynchronizingTables

class SynchronizingTablesTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(SynchronizingTables(3, [50, 1, 1024], [20000, 100000, 90000]),
                         [90000, 20000, 100000])
        self.assertEqual(SynchronizingTables(3, [30, 50, 40], [20000, 1900, 1900]),
                         [1900, 20000, 1900])

    def test_empty(self):
        self.assertEqual(SynchronizingTables(0, [], []),
                         [])

    def test_border(self):
        self.assertEqual(SynchronizingTables(1, [50], [20000]),
                         [20000])


if __name__ == '__main__':
    unittest.main()