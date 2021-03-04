import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.score_list = [1, 23, 65, 12, 99, 22, 65, 9]
    
    def test_latest(self):
        self.assertEqual(9, latest(self.score_list))
        
    def test_best(self):
        self.assertEqual(99, personal_best(self.score_list))

    def test_three_best(self):
        self.assertEqual([99, 65, 23], personal_top_three(self.score_list))

    def test_order_from_lowest(self):
        self.assertEqual([99, 65, 23, 22, 12, 9, 1], low_to_high(self.score_list))

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
