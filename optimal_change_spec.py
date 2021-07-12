# Write your unit tests here!
import unittest
from optimal_change import optimal_change

class OptimalChangeTestCase(unittest.TestCase):
    """Tests for the code"""
    def test_change_return_string(self):
        self.assertTrue(optimal_change(66.66, 80), 'The optimal change for this item is 13.13 with an amount paid of $80 is 1 $10 bill, 3 $1 bills, 1 dime and 3 pennies.' )

    def test_change_2(self):
        self.assertTrue(optimal_change(20, 20)) == "No Change."

    def test_change_3(self):
        self.assertTrue(optimal_change(100, 80)), "You dont have enough money for this purchase."

if __name__ == "__main__":
    unittest.main()