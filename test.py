import unittest
from simple_calc import Calculations

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')
        calculation = Calculations(100, 0)
        self.assertEqual(calculation.get_sum(), 100, 'The sum is wrong.')
        calculation = Calculations(525, -125)
        self.assertEqual(calculation.get_sum(), 400, 'The sum is wrong.')
        calculation = Calculations(0, 0)
        self.assertEqual(calculation.get_sum(), 0, 'The sum is wrong.')
        calculation = Calculations(100000000, 1)
        self.assertEqual(calculation.get_sum(), 100000001, 'The sum is wrong.')
    
    def test_diff(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_difference(), 6, 'The difference is wrong.')
        calculation = Calculations(100, 0)
        self.assertEqual(calculation.get_difference(), 100, 'The difference is wrong.')
        calculation = Calculations(0, 100)
        self.assertEqual(calculation.get_difference(), -100, 'The difference is wrong.')
        calculation = Calculations(100000000, 100000000)
        self.assertEqual(calculation.get_difference(), 0, 'The difference is wrong.')
        calculation = Calculations(0, 0)
        self.assertEqual(calculation.get_difference(), 0, 'The difference is wrong.')

    def test_prod(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_product(), 16, 'The product is wrong.')
        calculation = Calculations(8, 0)
        self.assertEqual(calculation.get_product(), 0, 'The product is wrong.')
        calculation = Calculations(0, 0)
        self.assertEqual(calculation.get_product(), 0, 'The product is wrong.')
        calculation = Calculations(100, 2)
        self.assertEqual(calculation.get_product(), 200, 'The product is wrong.')
    
    def test_quot(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_quotient(), 4, 'The quotient is wrong.')
        calculation = Calculations(0, 2)
        self.assertEqual(calculation.get_quotient(), 0, 'The quotient is wrong.')


if __name__ == '__main__':
    unittest.main()
