import unittest

from src.functions.loops import (
    add_pairwise,
    count_digits,
    count_down,
    factorial,
    fibonacci,
    is_prime,
    keys_above,
    multiplication_table,
    positions_of,
    sum_even,
    sum_skipping_negatives,
    sum_to,
    sum_until_zero,
)


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

    def test_count_digits_of_positive_numbers_and_boundaries(self):
        self.assertEqual(count_digits(9), 1)
        self.assertEqual(count_digits(10), 2)
        self.assertEqual(count_digits(99), 2)
        self.assertEqual(count_digits(100), 3)
        self.assertEqual(count_digits(99999), 5)

    def test_multiplication_table_default_limit(self):
        self.assertEqual(multiplication_table(2), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_fibonacci_short_sequences(self):
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])

    def test_break_stops_the_loop(self):
        self.assertEqual(sum_until_zero([1, 2, 0, 5]), 3)
        self.assertEqual(sum_until_zero([1, 2]), 3)
        self.assertEqual(sum_until_zero([0, 5]), 0)
        self.assertEqual(sum_until_zero([]), 0)
        # Only 0 stops the loop - negative numbers are added.
        self.assertEqual(sum_until_zero([3, -1, 2, 0, 9]), 4)

    def test_continue_skips_one_iteration(self):
        self.assertEqual(sum_skipping_negatives([1, -2, 3, -4]), 4)
        self.assertEqual(sum_skipping_negatives([-1]), 0)
        self.assertEqual(sum_skipping_negatives([0, 5]), 5)
        self.assertEqual(sum_skipping_negatives([0.5, -1.5]), 0.5)

    def test_for_else_prime_check(self):
        for number in (2, 3, 5, 97):
            self.assertIs(is_prime(number), True)
        # 25 and 91 (7 * 13) have no small even divisor - a loop that stops too early misses them.
        for number in (-7, -1, 0, 1, 4, 9, 25, 91):
            self.assertIs(is_prime(number), False)

    def test_enumerate_gives_index_and_value(self):
        self.assertEqual(positions_of([1, 2, 1, 3, 1], 1), [0, 2, 4])
        self.assertEqual(positions_of("abca", "a"), [0, 3])
        self.assertEqual(positions_of([5], 9), [])

    def test_zip_iterates_in_parallel(self):
        self.assertEqual(add_pairwise([1, 2, 3], [10, 20, 30]), [11, 22, 33])
        # zip stops at the shorter sequence.
        self.assertEqual(add_pairwise([1, 2, 3], [10]), [11])
        self.assertEqual(add_pairwise([], [1]), [])

    def test_loop_over_dict_items(self):
        # The keys come out in dict order - not alphabetical and not sorted by value.
        scores = {"Eve": 85, "Bob": 70, "Ann": 90, "Joe": 80}
        self.assertEqual(keys_above(scores, 80), ["Eve", "Ann"])
        self.assertEqual(keys_above({}, 0), [])

    def test_loops_over_nothing_give_empty_results(self):
        # range(1, n + 1) is empty for n below 1 - the loop body never runs.
        self.assertEqual(sum_to(-3), 0)
        self.assertEqual(count_down(-2), [])
        self.assertEqual(sum_even(-4), 0)
        self.assertEqual(fibonacci(-1), [])
        self.assertEqual(multiplication_table(3, 0), [])
        self.assertEqual(multiplication_table(3, -2), [])
