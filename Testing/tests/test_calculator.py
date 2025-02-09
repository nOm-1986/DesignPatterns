import unittest
import src.calculator as sc

class CalculatorTests(unittest.TestCase):
    
    def test_sum(self):
        assert sc.sum(10, 5) == 15
    
    def test_subtract(self):
        assert sc.subtract(9,7) == 2

    def test_multiply(self):
        assert sc.multiply(3, 3) == 9

    def test_division(self):
        assert sc.division(10, 2) == 5

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            sc.division(30, 0)
        