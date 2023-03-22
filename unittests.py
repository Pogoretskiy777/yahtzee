import yahtzee
import unittest

class TestDecisions(unittest.TestCase):
    def test_score(self):
        
        # testing upper section calculations
        
        self.assertEqual(3, yahtzee.calculate_score([1, 2, 3, 4, 5], 3))
        self.assertEqual(6, yahtzee.calculate_score([2, 2, 2, 4, 5], 2))
        
        # testing three of a kind function
        
        self.assertEqual(15, yahtzee.calculate_score([2, 2, 2, 4, 5], 9))
        self.assertEqual(21, yahtzee.calculate_score([4, 4, 4, 4, 5], 9))
        self.assertEqual(0, yahtzee.calculate_score([1, 2, 4, 4, 5], 9))
        
        # testing four of a kind function
        
        self.assertEqual(0, yahtzee.calculate_score([2, 2, 2, 4, 5], 10))
        self.assertEqual(21, yahtzee.calculate_score([4, 4, 4, 4, 5], 9))
        self.assertEqual(0, yahtzee.calculate_score([1, 2, 4, 4, 5], 9))
        
        # testing full house function
        
        self.assertEqual(25, yahtzee.calculate_score([1, 1, 1, 3, 3], 11))
        self.assertEqual(0, yahtzee.calculate_score([1, 1, 2, 3, 3], 11))
        self.assertEqual(0, yahtzee.calculate_score([1, 1, 1, 1, 1], 11))
        self.assertEqual(25, yahtzee.calculate_score([1, 1, 3, 3, 3], 11))
        
        # testing small straight function
        
        self.assertEqual(30, yahtzee.calculate_score([1, 2, 3, 4, 5], 12))
        self.assertEqual(30, yahtzee.calculate_score([1, 3, 4, 5, 6], 12))
        self.assertEqual(0, yahtzee.calculate_score([2, 4, 5, 6, 1], 12))
        self.assertEqual(0, yahtzee.calculate_score([1, 2, 4, 5, 2], 12))

        # testing large straight function
        
        self.assertEqual(40, yahtzee.calculate_score([1, 2, 3, 4, 5], 13))
        self.assertEqual(0, yahtzee.calculate_score([2, 2, 3, 4, 1], 13))
        self.assertEqual(40, yahtzee.calculate_score([6, 3, 5, 4, 2], 13))
        self.assertEqual(0, yahtzee.calculate_score([1, 2, 3, 4, 6], 13))
        
        # testing yahtzee category calculation
        
        self.assertEqual(50, yahtzee.calculate_score([1, 1, 1, 1, 1], 14))
        self.assertEqual(0, yahtzee.calculate_score([1, 2, 2, 2, 2], 14))

        # testing chance category calculation
        
        self.assertEqual(5, yahtzee.calculate_score([1, 1, 1, 1, 1], 15))
        self.assertEqual(14, yahtzee.calculate_score([1, 2, 3, 6, 2], 15))

unittest.main()