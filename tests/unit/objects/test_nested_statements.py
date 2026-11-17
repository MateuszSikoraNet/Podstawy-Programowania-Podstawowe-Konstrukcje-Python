import unittest

from src.objects.nested_statements import Matrix


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()

    def test_count_even_in_matrix(self):
        self.assertEqual(self.matrix.count_even_in_matrix([[1, 2], [4, 5]]), 2)
        self.assertEqual(self.matrix.count_even_in_matrix([]), 0)

    def test_flatten(self):
        self.assertEqual(self.matrix.flatten([[1, 2], [], [3]]), [1, 2, 3])

    def test_transpose(self):
        self.assertEqual(self.matrix.transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(self.matrix.transpose([]), [])

    def test_find_pairs_with_sum(self):
        self.assertEqual(self.matrix.find_pairs_with_sum([1, 2, 3, 4], 5), [(1, 4), (2, 3)])

    def test_classify_numbers(self):
        self.assertEqual(
            self.matrix.classify_numbers([-2, 0, 3]),
            {"negative": [-2], "zero": [0], "positive": [3]},
        )

