# https://github.com/Rishika-Joshi5/lab11-RJ-DD
# Partner 1: Rishika Joshi
# Partner 2: Diya Dipu Nair

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3, 1), 3)
        self.assertEqual(multiply(3, -1), -3)
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(mul(-4, 2), -8)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(4, 2), 2)
        self.assertEqual(div(2, 2), 1)
        self.assertEqual(div(1, 2), 0.5)
        self.assertAlmostEqual(div(3, -9), 0.33)
        self.assertEqual(div(-3, 10), -0.3)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            log(5, 0)
        with self.assertRaises(ValueError):
            log(2, -1)
        with self.assertRaises(ValueError):
            log(1, -10)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-9)
        with self.assertRaises(ValueError):
            square_root(-2)
        with self.assertRaises(ValueError):
            square_root(-100)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(100), 10)
        self.assertEqual(square_root(4), 2)


# Do not touch this
if __name__ == "__main__":
    unittest.main()