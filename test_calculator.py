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

# Do not touch this
if __name__ == "__main__":
    unittest.main()
