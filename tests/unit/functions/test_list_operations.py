import unittest

from src.functions.list_operations import (
    average,
    filter_even,
    find_max,
    find_min,
    index_of,
    remove_duplicates,
    reverse_list,
    sort_descending,
)


class TestListOperations(unittest.TestCase):
    def test_find_extremes_and_average(self):
        self.assertEqual(find_max([3, 1, 5]), 5)
        self.assertEqual(find_min([3, 1, 5]), 1)
        self.assertEqual(average([2, 4, 6]), 4)

    def test_empty_list_raises_value_error_for_aggregates(self):
        with self.assertRaises(ValueError):
            find_max([])
        with self.assertRaises(ValueError):
            find_min([])
        with self.assertRaises(ValueError):
            average([])

    def test_list_transformations(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(remove_duplicates([1, 2, 1, 3]), [1, 2, 3])
        self.assertEqual(filter_even([1, 2, 4, 5]), [2, 4])
        self.assertEqual(sort_descending([2, 5, 1]), [5, 2, 1])

    def test_index_of(self):
        self.assertEqual(index_of([4, 5, 4], 4), 0)
        self.assertEqual(index_of([4, 5, 4], 9), -1)

