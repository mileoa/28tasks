import unittest
import random

from TheRabbitsFoot import TheRabbitsFoot

class TheRabbitsFootTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TheRabbitsFoot("отдай мою кроличью лапку", True), "омоюу толл дюиа акчп йрьк")
        self.assertEqual(TheRabbitsFoot("омоюу толл дюиа акчп йрьк", False), "отдаймоюкроличьюлапку")
        self.assertEqual(TheRabbitsFoot("привет", True), "пв ре ит")
        self.assertEqual(TheRabbitsFoot("пв ре ит", False), "привет")

    def test_border(self):
        self.assertEqual(TheRabbitsFoot("п ", True), "п")
        self.assertEqual(TheRabbitsFoot("п т", False), "пт")
        self.assertEqual(TheRabbitsFoot("п т", True), "п т")

if __name__ == '__main__':
    unittest.main()