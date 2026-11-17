import unittest

from src.objects.comparisons import Comparator


class TestComparator(unittest.TestCase):
    def setUp(self):
        self.comparator = Comparator()

    def test_basic_comparisons(self):
        self.assertTrue(self.comparator.is_equal(3, 3))
        self.assertTrue(self.comparator.is_greater(4, 3))
        self.assertTrue(self.comparator.is_less(2, 3))

    def test_is_between_includes_boundaries(self):
        self.assertTrue(self.comparator.is_between(3, 3, 5))
        self.assertTrue(self.comparator.is_between(5, 3, 5))
        self.assertFalse(self.comparator.is_between(6, 3, 5))

    def test_compare(self):
        self.assertEqual(self.comparator.compare(2, 3), "less")
        self.assertEqual(self.comparator.compare(3, 3), "equal")
        self.assertEqual(self.comparator.compare(4, 3), "greater")

    def test_are_all_equal(self):
        self.assertTrue(self.comparator.are_all_equal([2, 2, 2]))
        self.assertFalse(self.comparator.are_all_equal([2, 3]))
        self.assertTrue(self.comparator.are_all_equal([]))

    def test_max_of_three(self):
        self.assertEqual(self.comparator.max_of_three(2, 9, 4), 9)
        self.assertEqual(self.comparator.max_of_three(5, 5, 1), 5)

