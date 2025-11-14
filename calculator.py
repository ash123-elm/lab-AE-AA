# https://github.com/your-username/your-repo
# Partner 1: Your Name
# Partner 2: Partner Name
import unittest
import calculator
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


class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5, 0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -8)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
