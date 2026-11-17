import unittest

from src.functions.operators import (
    divide_with_remainder,
    floor_divide,
    is_even,
    is_odd,
    logical_and,
    logical_not,
    logical_or,
    modulo,
    power,
)


class TestOperators(unittest.TestCase):
    def test_arithmetic_operators(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(floor_divide(10, 3), 3)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(divide_with_remainder(10, 3), (3, 1))

    def test_even_and_odd(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(4))

    def test_logical_operators(self):
        self.assertFalse(logical_and(True, False))
        self.assertTrue(logical_or(False, True))
        self.assertFalse(logical_not(True))

    def test_division_by_zero_raises_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            floor_divide(10, 0)

