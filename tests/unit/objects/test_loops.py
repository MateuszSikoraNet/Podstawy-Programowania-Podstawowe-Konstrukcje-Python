import unittest

from src.objects.loops import LoopOperations


class TestLoopOperations(unittest.TestCase):
    def setUp(self):
        self.operations = LoopOperations()

    def test_sum_to_and_factorial(self):
        self.assertEqual(self.operations.sum_to(5), 15)
        self.assertEqual(self.operations.sum_to(0), 0)
        self.assertEqual(self.operations.factorial(5), 120)
        self.assertEqual(self.operations.factorial(0), 1)

    def test_negative_factorial_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.operations.factorial(-1)

    def test_count_down_and_digits(self):
        self.assertEqual(self.operations.count_down(4), [4, 3, 2, 1])
        self.assertEqual(self.operations.count_down(0), [])
        self.assertEqual(self.operations.count_digits(0), 1)
        self.assertEqual(self.operations.count_digits(-123), 3)

    def test_multiplication_table(self):
        self.assertEqual(self.operations.multiplication_table(3, 4), [3, 6, 9, 12])

    def test_sum_even(self):
        self.assertEqual(self.operations.sum_even(8), 20)
        self.assertEqual(self.operations.sum_even(1), 0)

    def test_fibonacci(self):
        self.assertEqual(self.operations.fibonacci(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(self.operations.fibonacci(0), [])

