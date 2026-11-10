import unittest

from src.functions.loops import count_digits, count_down, factorial, fibonacci, multiplication_table, sum_even, sum_to


class TestLoops(unittest.TestCase):
    def test_sum_to_and_factorial(self):
        self.assertEqual(sum_to(5), 15)
        self.assertEqual(sum_to(0), 0)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_negative_factorial_raises_value_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_count_down_and_digits(self):
        self.assertEqual(count_down(4), [4, 3, 2, 1])
        self.assertEqual(count_down(0), [])
        self.assertEqual(count_digits(0), 1)
        self.assertEqual(count_digits(-123), 3)

    def test_multiplication_table(self):
        self.assertEqual(multiplication_table(3, 4), [3, 6, 9, 12])

    def test_sum_even(self):
        self.assertEqual(sum_even(8), 20)
        self.assertEqual(sum_even(1), 0)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fibonacci(0), [])

