import unittest

from src.objects.operators import OperatorCalculator


class TestOperatorCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = OperatorCalculator()

    def test_arithmetic_operators(self):
        self.assertEqual(self.calculator.modulo(10, 3), 1)
        self.assertEqual(self.calculator.floor_divide(10, 3), 3)
        self.assertEqual(self.calculator.power(2, 3), 8)
        self.assertEqual(self.calculator.power(5, 0), 1)
        self.assertEqual(self.calculator.divide_with_remainder(10, 3), (3, 1))

    def test_even_and_odd(self):
        self.assertTrue(self.calculator.is_even(4))
        self.assertFalse(self.calculator.is_even(3))
        self.assertTrue(self.calculator.is_odd(3))
        self.assertFalse(self.calculator.is_odd(4))

    def test_logical_operators(self):
        self.assertFalse(self.calculator.logical_and(True, False))
        self.assertTrue(self.calculator.logical_or(False, True))
        self.assertFalse(self.calculator.logical_not(True))

    def test_division_by_zero_raises_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.floor_divide(10, 0)

