import unittest

from src.objects.list_operations import NumberList


class TestNumberList(unittest.TestCase):
    def setUp(self):
        self.numbers = NumberList([3, 1, 5, 1])

    def test_find_extremes_and_average(self):
        self.assertEqual(self.numbers.find_max(), 5)
        self.assertEqual(self.numbers.find_min(), 1)
        self.assertEqual(self.numbers.average(), 2.5)

    def test_empty_list_raises_value_error_for_aggregates(self):
        numbers = NumberList()
        with self.assertRaises(ValueError):
            numbers.find_max()
        with self.assertRaises(ValueError):
            numbers.find_min()
        with self.assertRaises(ValueError):
            numbers.average()

    def test_list_transformations(self):
        self.assertEqual(self.numbers.reverse(), [1, 5, 1, 3])
        self.assertEqual(self.numbers.remove_duplicates(), [3, 1, 5])
        self.assertEqual(self.numbers.filter_even(), [])
        self.assertEqual(self.numbers.sort_descending(), [5, 3, 1, 1])

    def test_index_of(self):
        self.assertEqual(self.numbers.index_of(1), 1)
        self.assertEqual(self.numbers.index_of(9), -1)

