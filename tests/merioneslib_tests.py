# MerionesLib_tests.py
# Projekt IVS II.
# Autor: Jaromír Wysoglad, xwysog00
# Datum: 2018-03-26

import unittest

from src.merionesmathlib import MerionesLib


# To run tests, go to the parent directory and
# type "python3 -m tests.merioneslib_tests.py"

# Tests the add function (+)
class MerionesLibTestAdd(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_add_positive(self):
        self.assertEqual(self.math.add(1, 2), 3)
        self.assertEqual(self.math.add(0, 0), 0)
        self.assertEqual(self.math.add(0, 2), 2)
        self.assertEqual(self.math.add(58, 72), 130)

    def test_add_negative(self):
        self.assertEqual(self.math.add(-1, -1), -2)
        self.assertEqual(self.math.add(0, -5), -5)
        self.assertEqual(self.math.add(-5, 0), -5)
        self.assertEqual(self.math.add(-58, -72), -130)

    def test_add_positive_negative(self):
        self.assertEqual(self.math.add(-5, 2), -3)
        self.assertEqual(self.math.add(5, -7), -2)
        self.assertEqual(self.math.add(-7, 8), 1)
        self.assertEqual(self.math.add(-7, 7), 0)

    def test_add_decimal(self):
        self.assertEqual(self.math.add(2.25, 4.5), 6.75)
        self.assertEqual(self.math.add(-2.25, 4.5), 2.25)
        self.assertEqual(self.math.add(-2.25, -4.5), -6.75)


# Tests the sub function (-)
class MerionesLibTestSub(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_sub_positive(self):
        self.assertEqual(self.math.sub(1, 2), -1)
        self.assertEqual(self.math.sub(0, 0), 0)
        self.assertEqual(self.math.sub(0, 2), -2)
        self.assertEqual(self.math.sub(72, 58), 14)

    def test_sub_negative(self):
        self.assertEqual(self.math.sub(-1, -1), 0)
        self.assertEqual(self.math.sub(0, -5), 5)
        self.assertEqual(self.math.sub(-5, 0), -5)
        self.assertEqual(self.math.sub(-58, -72), 14)

    def test_sub_positive_negative(self):
        self.assertEqual(self.math.sub(-5, 2), -7)
        self.assertEqual(self.math.sub(5, -7), 12)
        self.assertEqual(self.math.sub(-7, 8), -15)
        self.assertEqual(self.math.sub(7, 8), -1)

    def test_sub_decimal(self):
        self.assertEqual(self.math.sub(2.25, 4.5), -2.25)
        self.assertEqual(self.math.sub(-2.25, 4.5), -6.75)
        self.assertEqual(self.math.sub(-2.25, -4.5), 2.25)


# Tests the mul function (*)
class MerionesLibTestMul(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_mul_positive(self):
        self.assertEqual(self.math.mul(1, 2), 2)
        self.assertEqual(self.math.mul(0, 0), 0)
        self.assertEqual(self.math.mul(0, 2), 0)
        self.assertEqual(self.math.mul(72, 58), 4176)

    def test_mul_negative(self):
        self.assertEqual(self.math.mul(-1, -1), 1)
        self.assertEqual(self.math.mul(0, -5), 0)
        self.assertEqual(self.math.mul(-5, 0), 0)
        self.assertEqual(self.math.mul(-58, -72), 4176)

    def test_mul_positive_negative(self):
        self.assertEqual(self.math.mul(-5, 2), -10)
        self.assertEqual(self.math.mul(5, -7), -35)
        self.assertEqual(self.math.mul(-7, 8), -56)
        self.assertEqual(self.math.mul(7, 8), 56)

    def test_mul_positive_decimal(self):
        self.assertEqual(self.math.mul(1.5, 3.25), 4.875)
        self.assertEqual(self.math.mul(-1.5, 3.25), -4.875)
        self.assertEqual(self.math.mul(-1.5, -3.25), 4.875)


# Tests the div function (/)
class MerionesLibTestDiv(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    # Division by zero is usually forbidden in math
    def test_div_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.math.div(10,0)

    def test_div_positive(self):
        self.assertEqual(self.math.div(10, 2), 5)
        self.assertEqual(self.math.div(42, 21), 2)
        self.assertEqual(self.math.div(0, 2), 0)
        self.assertEqual(self.math.div(1024, 1024), 1)

    def test_div_negative(self):
        self.assertEqual(self.math.div(-1, -1), 1)
        self.assertEqual(self.math.div(0, -5), 0)
        self.assertEqual(self.math.div(-10, -2), 5)
        self.assertEqual(self.math.div(-42, -21), 2)

    def test_div_positive_negative(self):
        self.assertEqual(self.math.div(-10, 2), -5)
        self.assertEqual(self.math.div(42, -21), -2)
        self.assertEqual(self.math.div(-7, 7), -1)

    def test_div_decimal(self):
        self.assertEqual(self.math.div(4.875, 3.25), 1.5)
        self.assertEqual(self.math.div(-10, 2.5), -4)
        self.assertAlmostEqual(self.math.div(-10, -3), 3.3333, 4)


# Tests the pow function (^)
class MerionesLibTestPow(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    # Anything to the power of zero is always 1
    def test_pow_power_of_zero(self):
        self.assertEqual(self.math.pow(185, 0), 1)

    def test_pow_positive_even(self):
        self.assertEqual(self.math.pow(-10, 2), 100)
        self.assertEqual(self.math.pow(5, 4), 625)
        self.assertEqual(self.math.pow(0, 2), 0)

    def test_pow_positive_odd(self):
        self.assertEqual(self.math.pow(-1, 3), -1)
        self.assertEqual(self.math.pow(2, 5), 32)
        self.assertEqual(self.math.pow(-10, 1), -10)

    def test_pow_negative(self):
        self.assertEqual(self.math.pow(2, -1), 0.5)
        self.assertEqual(self.math.pow(4, -2), 0.0625)
        self.assertEqual(self.math.pow(1, -10), 1)

    def test_pow_decimal(self):
        self.assertEqual(self.math.pow(1, 3.25), 1)
        self.assertEqual(self.math.pow(-25, 2.5), 3125)
        self.assertEqual(self.math.pow(4, -0.5), 0.5)


# Tests the root function (√)
class MerionesLibTestRoot(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    # Even root of negative number is usually forbidden in math
    def test_root_even_root_of_negative(self):
        with self.assertRaises(ValueError):
            self.math.root(4, -4)

        with self.assertRaises(ValueError):
            self.math.root(10, -2)

    def test_root_of_positive(self):
        self.assertEqual(self.math.root(100, 2), 10)
        self.assertEqual(self.math.root(9, 3), 3)
        self.assertEqual(self.math.root(0, 2), 0)

    def test_root_odd_root_of_negative(self):
        self.assertEqual(self.math.root(-1, 3), -1)
        self.assertEqual(self.math.root(-512, 9), -2)
        self.assertEqual(self.math.root(-10, 1), -10)

    def test_root_negative_root(self):
        self.assertEqual(self.math.root(2, -1), 0.5)
        self.assertEqual(self.math.root(4, -2), 0.5)
        self.assertEqual(self.math.root(1, -10), 1)

    def test_root_decimal(self):
        self.assertEqual(self.math.root(4.875, 3.25), 172.1542)
        self.assertEqual(self.math.root(3125, 2.5), 25)
        self.assertEqual(self.math.root(0.5, -0.5), 4)


# Tests the factorial function (!)
class MerionesLibTestFactorial(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    # Factorial of negative number is forbidden in math
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            self.math.factorial(-5)
        with self.assertRaises(ValueError):
            self.math.factorial(-1)

    # Factorial of decimal number is usually forbidden in math
    def test_factorial_decimal(self):
        with self.assertRaises(ValueError):
            self.math.factorial(1.5)
        with self.assertRaises(ValueError):
            self.math.factorial(-2.89)

    # Factorial of zero is 1 by definition
    def test_factorial_of_zero(self):
        self.assertEqual(self.math.factorial(0), 1)

    def test_factorial_of_positive(self):
        self.assertEqual(self.math.factorial(1), 1)
        self.assertEqual(self.math.factorial(5), 120)
        self.assertEqual(self.math.factorial(10), 3628800)


# Tests the solve_expression function
class MerionesLibTestSolveExpression(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_solve_expression_addition(self):
        self.assertEqual(self.math.solve_expression("5+8"), 13)
        self.assertEqual(self.math.solve_expression("-10+19"), 9)
        self.assertEqual(self.math.solve_expression("5+-9"), -4)
        self.assertEqual(self.math.solve_expression("4.5+10"), 14.5)
        self.assertEqual(self.math.solve_expression("9+-4.5"), 4.5)

    def test_solve_expression_subtraction(self):
        self.assertEqual(self.math.solve_expression("5-8"), -3)
        self.assertEqual(self.math.solve_expression("-10-19"), -29)
        self.assertEqual(self.math.solve_expression("5--9"), 14)
        self.assertEqual(self.math.solve_expression("4.5-10"), -6.5)
        self.assertEqual(self.math.solve_expression("9-4.5"), 4.5)

    def test_solve_expression_multiplication(self):
        self.assertEqual(self.math.solve_expression("5*8"), 40)
        self.assertEqual(self.math.solve_expression("-10*19"), -190)
        self.assertEqual(self.math.solve_expression("5*-9"), -45)
        self.assertEqual(self.math.solve_expression("4.5*10"), 45)
        self.assertEqual(self.math.solve_expression("9*-4.5"), -40.5)

    def test_solve_expression_division(self):
        self.assertEqual(self.math.solve_expression("5/8"), 0.625)
        self.assertEqual(self.math.solve_expression("-10/5"), -2)
        self.assertEqual(self.math.solve_expression("5/-25"), -0.2)
        self.assertEqual(self.math.solve_expression("4.5/10"), 0.45)
        self.assertEqual(self.math.solve_expression("9/-4.5"), -2)

        # Division by zero is forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("-5/0")

    def test_solve_expression_power(self):
        self.assertEqual(self.math.solve_expression("5^8"), 390625)
        self.assertEqual(self.math.solve_expression("-10^5"), -100000)
        self.assertEqual(self.math.solve_expression("-10^4"), 10000)
        self.assertEqual(self.math.solve_expression("5^-3"), 0.008)
        self.assertEqual(self.math.solve_expression("4.5^5"), 1845.28125)
        self.assertEqual(self.math.solve_expression("9^0"), 1)

    def test_solve_expression_root(self):
        self.assertEqual(self.math.solve_expression("3√8"), 2)
        self.assertEqual(self.math.solve_expression("√16"), 4)
        self.assertEqual(self.math.solve_expression("3√-125"), -5)
        self.assertEqual(self.math.solve_expression("-5√100000"), -10)
        self.assertEqual(self.math.solve_expression("3√12,167"), 2.3)

        # Even root of negative number is forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("4√-2")
        with self.assertRaises(ValueError):
            self.math.solve_expression("√-2")

    def test_solve_expression_factorial(self):
        self.assertEqual(self.math.solve_expression("0!"), 1)
        self.assertEqual(self.math.solve_expression("1!"), 1)
        self.assertEqual(self.math.solve_expression("2!"), 2)
        self.assertEqual(self.math.solve_expression("5!"), 120)

        # Factorials of negative nad decimal numbers are forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("0.5!")
        with self.assertRaises(ValueError):
            self.math.solve_expression("-1!")

    def test_solve_expression_multiple_operations(self):
        self.assertEqual(self.math.solve_expression("5+8/2*10"), 45)
        self.assertEqual(self.math.solve_expression("5^2+10*2"), 45)
        self.assertEqual(self.math.solve_expression("2!*8+1"), 17)
        self.assertEqual(self.math.solve_expression("1*5/5+1-1*3/3^1"), 1)
        with self.assertRaises(ValueError):
            self.math.solve_expression("2!*8+1/0")
        with self.assertRaises(ValueError):
            self.math.solve_expression("2!*8+1--1!")


if __name__ == '__main__':
    unittest.main()
