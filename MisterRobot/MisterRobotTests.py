import unittest
import random
import time

from MisterRobot import MisterRobot

class MisterRobotTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(MisterRobot(7, [1,3,4,5,6,2,7]), True)
        self.assertEqual(MisterRobot(7, [3,5,1,6,4,7,2]), False)
        self.assertEqual(MisterRobot(5, [1,5,4,2,3]), False)
        self.assertEqual(MisterRobot(5, [2,5,4,1,3]), True)
        self.assertEqual(MisterRobot(10, [8,1,2,9,4,10,3,7,6,5]), False)
        self.assertEqual(MisterRobot(10, [1,4,10,5,2,3,8,6,9,7]), True)

    def test_execution_time(self):
        for i in range(100000):
            l = [i+1 for i in range(10)]
            random.shuffle(l)
            startTime = time.time()
            MisterRobot(10, l)
            self.assertLessEqual(time.time() - startTime, 1)

if __name__ == '__main__':
    unittest.main()
