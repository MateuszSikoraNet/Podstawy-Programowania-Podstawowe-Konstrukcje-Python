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

    def test_extremes_of_negative_numbers(self):
        numbers = NumberList([-3, -1, -5])
        self.assertEqual(numbers.find_max(), -1)
        self.assertEqual(numbers.find_min(), -5)
        self.assertEqual(NumberList([4, 2, 6]).find_min(), 2)

    def test_filter_even_keeps_even_numbers(self):
        self.assertEqual(NumberList([1, 2, 3, 4, -6]).filter_even(), [2, 4, -6])

    def test_methods_do_not_change_the_numbers(self):
        numbers = NumberList([3, 1, 2])
        self.assertEqual(numbers.sort_descending(), [3, 2, 1])
        self.assertEqual(numbers.reverse(), [2, 1, 3])
        self.assertEqual(numbers.numbers, [3, 1, 2])

    def test_each_object_gets_its_own_empty_list(self):
        # A [] default would be shared by every NumberList() - use None and create a new list.
        first = NumberList()
        first.numbers.append(5)
        self.assertEqual(NumberList().numbers, [])
