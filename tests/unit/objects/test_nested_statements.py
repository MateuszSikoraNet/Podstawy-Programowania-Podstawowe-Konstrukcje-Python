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

    def test_count_even_in_matrix_counts_every_even_value(self):
        # Rows of different lengths; zero and negative even numbers count too.
        self.assertEqual(self.matrix.count_even_in_matrix([[2, 4, 6], [1]]), 3)
        self.assertEqual(self.matrix.count_even_in_matrix([[0, -2, -3], [8, 10]]), 4)
        self.assertEqual(self.matrix.count_even_in_matrix([[1, 3], [5]]), 0)

    def test_flatten_edge_cases(self):
        self.assertEqual(self.matrix.flatten([]), [])
        self.assertEqual(self.matrix.flatten([[], []]), [])
        self.assertEqual(self.matrix.flatten([[1], [2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_transpose_square_and_single_row(self):
        self.assertEqual(self.matrix.transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])
        self.assertEqual(self.matrix.transpose([[1, 2, 3]]), [[1], [2], [3]])
        self.assertEqual(self.matrix.transpose([[1], [2]]), [[1, 2]])

    def test_find_pairs_uses_each_position_once(self):
        # The inner loop starts after the outer index: no element is paired with itself...
        self.assertEqual(self.matrix.find_pairs_with_sum([1, 2, 3], 4), [(1, 3)])
        # ...but equal values at different positions do form a pair.
        self.assertEqual(self.matrix.find_pairs_with_sum([2, 2], 4), [(2, 2)])
        self.assertEqual(self.matrix.find_pairs_with_sum([1, 3, 3], 4), [(1, 3), (1, 3)])
        self.assertEqual(self.matrix.find_pairs_with_sum([1, 2], 10), [])

    def test_classify_numbers_keeps_order_and_duplicates(self):
        self.assertEqual(
            self.matrix.classify_numbers([5, -1, 0, 3, -4, 0, 5]),
            {"negative": [-1, -4], "zero": [0, 0], "positive": [5, 3, 5]},
        )

    def test_break_leaves_only_the_inner_loop(self):
        # 0 is not negative; -1 is.
        self.assertEqual(self.matrix.first_negative_per_row([[1, -2, -3], [4, 5], [-6], [0, -1]]), [-2, None, -6, -1])
        self.assertEqual(self.matrix.first_negative_per_row([]), [])

    def test_exit_both_loops(self):
        self.assertEqual(self.matrix.find_in_matrix([[1, 2], [3, 2]], 2), (0, 1))
        self.assertEqual(self.matrix.find_in_matrix([[1, 2], [3, 2]], 3), (1, 0))
        # Row by row, not column by column.
        self.assertEqual(self.matrix.find_in_matrix([[5, 1], [1, 5]], 1), (0, 1))
        self.assertIsNone(self.matrix.find_in_matrix([[1, 2]], 9))
        self.assertIsNone(self.matrix.find_in_matrix([], 1))

    def test_try_inside_loop_skips_only_bad_values(self):
        self.assertEqual(self.matrix.sum_valid_numbers(["1", "x", "2", " 3 ", "4.5"]), 6)
        self.assertEqual(self.matrix.sum_valid_numbers(["a"]), 0)
        self.assertEqual(self.matrix.sum_valid_numbers([]), 0)

    def test_classify_numbers_always_has_all_groups(self):
        self.assertEqual(self.matrix.classify_numbers([5]), {"negative": [], "zero": [], "positive": [5]})
        self.assertEqual(self.matrix.classify_numbers([]), {"negative": [], "zero": [], "positive": []})

    def test_find_pairs_keeps_list_order(self):
        self.assertEqual(self.matrix.find_pairs_with_sum([4, 1, 3, 2], 5), [(4, 1), (3, 2)])

    def test_sum_valid_numbers_accepts_negative_integers(self):
        # int() accepts a sign - str.isdigit() does not.
        self.assertEqual(self.matrix.sum_valid_numbers(["-2", "5", "+1"]), 4)
