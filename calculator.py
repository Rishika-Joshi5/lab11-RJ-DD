"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/Rishika-Joshi5/lab11-RJ-DD
# Partner 1:
# Partner 2: Diya Dipu Nair

import math
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def log(a, b):
    if b <= 0:
        raise ValueError
    return math.log(b, a)
def exp(a, b):
    return a ** b
