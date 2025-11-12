# https://github.com/Rishika-Joshi5/lab11-RJ-DD
# Partner 1: Rishika Joshi
# Partner 2: Diya Dipu Nair


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-3, -3), -6)

        self.assertNotEqual(add(2, 2), 6)
        self.assertNotEqual(add(-2, 2), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-3, -3), 0)
        self.assertNotEqual(subtract(8, -3), 5)
        self.assertEqual(subtract(4, 8), -4)

        self.assertNotEqual(subtract(6, 3), 4)
        self.assertNotEqual(subtract(-6, 3), -9)


    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 2), -4)
        self.assertEqual(mul(-4, -4), 16)

        self.assertNotEqual(mul(3, 3), 8)
        self.assertNotEqual(mul(-3, 3), 9)
        self.assertNotEqual(mul(8, 3), 5)
        self.assertNotEqual(mul(4, 8), -4)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(6, 3), 0.5)
        self.assertEqual(div(-3, -3), 1)
        self.assertEqual(div(2, 10), 5)

        self.assertNotEqual(div(2, 2), -2)
        self.assertNotEqual(div(-3, -3), 0)
        self.assertNotEqual(div(10, 3), 5)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

        self.assertNotEqual(div(10, 2), 6)
        self.assertNotEqual(div(-10, 2), 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(3, 9), 2)
        self.assertEqual(logarithm(5, 25), 2)
        self.assertEqual(logarithm(2, 16), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-5, 5)



    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(2, -5)
        with self.assertRaises(ValueError):
            logarithm(3, 0)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertEqual(hypotenuse(9, 12), 15)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(4), 2)

# Do not touch this
if __name__ == "__main__":
    unittest.main()