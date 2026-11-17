import unittest

from src.functions.nested_statements import classify_numbers, count_even_in_matrix, find_pairs_with_sum, flatten, transpose


class TestNestedStatements(unittest.TestCase):
    def test_count_even_in_matrix(self):
        self.assertEqual(count_even_in_matrix([[1, 2], [4, 5]]), 2)
        self.assertEqual(count_even_in_matrix([]), 0)

    def test_flatten(self):
        self.assertEqual(flatten([[1, 2], [], [3]]), [1, 2, 3])

    def test_transpose(self):
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(transpose([]), [])

    def test_find_pairs_with_sum(self):
        self.assertEqual(find_pairs_with_sum([1, 2, 3, 4], 5), [(1, 4), (2, 3)])

    def test_classify_numbers(self):
        self.assertEqual(
            classify_numbers([-2, 0, 3]),
            {"negative": [-2], "zero": [0], "positive": [3]},
        )

