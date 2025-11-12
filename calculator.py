"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError

    return a / b


def log(a, b):
    if b <= 0:
        raise ValueError
    return math.log(a, b)



def pow(a, b):
    return math.pow(a, b)

