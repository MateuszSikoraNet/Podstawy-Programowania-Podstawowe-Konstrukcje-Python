import unittest
from src.functions.calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_divide_numbers(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_operations_on_floats(self):
        self.assertEqual(add(1.5, 2), 3.5)
        self.assertEqual(multiply(1.5, 3), 4.5)

    def test_subtract_order_matters(self):
        self.assertEqual(subtract(4, 10), -6)

    def test_divide_is_true_division(self):
        self.assertEqual(divide(7, 2), 3.5)
