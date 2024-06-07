import unittest
import random

from ConquestCampaign import ConquestCampaign

class ConquestCampaignTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(ConquestCampaign(3, 4, 2, [2,2, 3,4]), 3)
        
    def test_border(self):
        self.assertEqual(ConquestCampaign(1, 1, 1, [1, 1]), 1)
        self.assertEqual(ConquestCampaign(2, 1, 1, [1, 1]), 2)
        self.assertEqual(ConquestCampaign(1, 3, 1, [1, 1]), 3)

if __name__ == '__main__':
    unittest.main()