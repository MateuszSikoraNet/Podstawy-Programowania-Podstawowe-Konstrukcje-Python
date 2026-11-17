import unittest

from src.functions.comparisons import are_all_equal, compare, is_between, is_equal, is_greater, is_less, max_of_three


class TestComparisons(unittest.TestCase):
    def test_basic_comparisons(self):
        self.assertTrue(is_equal(3, 3))
        self.assertTrue(is_greater(4, 3))
        self.assertTrue(is_less(2, 3))

    def test_is_between_includes_boundaries(self):
        self.assertTrue(is_between(3, 3, 5))
        self.assertTrue(is_between(5, 3, 5))
        self.assertFalse(is_between(6, 3, 5))

    def test_compare(self):
        self.assertEqual(compare(2, 3), "less")
        self.assertEqual(compare(3, 3), "equal")
        self.assertEqual(compare(4, 3), "greater")

    def test_are_all_equal(self):
        self.assertTrue(are_all_equal([2, 2, 2]))
        self.assertFalse(are_all_equal([2, 3]))
        self.assertTrue(are_all_equal([]))

    def test_max_of_three(self):
        self.assertEqual(max_of_three(2, 9, 4), 9)
        self.assertEqual(max_of_three(5, 5, 1), 5)

