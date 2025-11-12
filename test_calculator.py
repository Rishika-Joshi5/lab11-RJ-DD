# https://github.com/Rishika-Joshi5/lab11-RJ-DD
# Partner 1:
# Partner 2: Diya Dipu Nair


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-3, -3), 0)

        self.assertNotEqual(add(2, 2), 6)
        self.assertNotEqual(add(-2, 2), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5, 2), 3)
        self.assertEqual(sub(-6, 3), -3)
        self.assertEqual(sub(-3, -3), 0)
        self.assertEqual(sub(8, -3), 5)
        self.assertEqual(sub(4, 8), -4)

        self.assertNotEqual(sub(6, 3), 4)
        self.assertNotEqual(sub(-6, 3), -3)


    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

        self.assertNotEqual(div(10, 2), 6)
        self.assertNotEqual(div(-10, 2), 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(3, 9), 2)
        self.assertEqual(log(5, 25), 2)
        self.assertEqual(log(2, 16), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-5, 5)

        self.assertNotEqual(log(-5, 7), 0)
        self.assertNotEqual(log(-5, 3), 25)
        self.assertNotEqual(log(-5, 6), 3)

    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()