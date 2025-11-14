# https://github.com/ash123-elm/lab-AE-AA.git
# Partner 1: Asher Elman
# Partner 2: Aidan Arjune

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-2, 8)
        with self.assertRaises(ValueError):
            logarithm(2, -8)
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-2, 7), 5)
        self.assertEqual(add(-4, -6), -10)

    def test_subtract(self):
        self.assertEqual(sub(10, 3), 7)
        self.assertEqual(sub(5, 10), -5)
        self.assertEqual(sub(-4, -2), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(9, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 1000), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(-3, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 10)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
