# https://github.com/ash123-elm/lab-AE-AA.git
# Partner 1: Asher Elman
# Partner 2: Aidan Arjune

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Specified behavior: return b / a ; raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero (divisor 'a' was 0)")
    return b / a

def logarithm(a, b):
    # return log base a of b
    # both base and argument must be positive, base != 1
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm base and argument must be positive")
    if a == 1:
        raise ValueError("Logarithm base cannot be 1")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    # returns sqrt(a² + b²)
    return math.sqrt(a**2 + b**2)
