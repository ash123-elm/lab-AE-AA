# https://github.com/your-username/your-repo
# Partner 1: Your Name
# Partner 2: Partner Name

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # Specified behavior: return b / a ; raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero (divisor 'a' was 0)")
    return b / a

def log(a, b):
    # return log base a of b
    # both base and argument must be positive, base != 1
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm base and argument must be positive")
    if a == 1:
        raise ValueError("Logarithm base cannot be 1")
    return math.log(b, a)

def exp(a, b):
    return a ** b
