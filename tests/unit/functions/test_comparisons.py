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

    def test_basic_comparisons_false_cases(self):
        # A check gives False when the condition does not hold - also for equal values.
        self.assertIs(is_equal(3, 4), False)
        self.assertIs(is_greater(3, 3), False)
        self.assertIs(is_greater(2, 3), False)
        self.assertIs(is_less(3, 3), False)
        self.assertIs(is_less(4, 3), False)

    def test_is_between_excludes_values_below_lower(self):
        self.assertIs(is_between(2, 3, 5), False)
        self.assertIs(is_between(4, 3, 5), True)
        self.assertIs(is_between(4.5, 3, 5), True)

    def test_are_all_equal_checks_every_value(self):
        self.assertIs(are_all_equal([2, 2, 3]), False)
        self.assertIs(are_all_equal([3, 2, 2]), False)
        self.assertIs(are_all_equal([7]), True)

    def test_max_of_three_in_any_position(self):
        self.assertEqual(max_of_three(9, 2, 4), 9)
        self.assertEqual(max_of_three(1, 2, 9), 9)
        self.assertEqual(max_of_three(-5, -1, -3), -1)
        self.assertEqual(max_of_three(1, 5, 5), 5)

    def test_equality_of_different_types_is_false_not_error(self):
        # == never raises for unrelated types, it just returns False (ordering with < raises TypeError).
        self.assertIs(is_equal(1, "1"), False)
        self.assertIs(is_equal(None, 0), False)
        self.assertIs(is_equal(1, 1.0), True)

    def test_equality_of_containers_compares_values(self):
        # == compares contents, not identity; order matters for lists, not for sets and dicts.
        self.assertIs(is_equal([1, 2], [1, 2]), True)
        self.assertIs(is_equal([1, 2], [2, 1]), False)
        self.assertIs(is_equal({1, 2}, {2, 1}), True)
        self.assertIs(is_equal({"a": 1, "b": 2}, {"b": 2, "a": 1}), True)
        # A tuple is never equal to a list, even with the same elements.
        self.assertIs(is_equal((1, 2), [1, 2]), False)

    def test_compare_works_for_any_ordered_type(self):
        # Use comparison operators, not subtraction - "apple" - "banana" raises TypeError.
        self.assertEqual(compare("apple", "banana"), "less")
        self.assertEqual(compare("b", "b"), "equal")
        self.assertEqual(compare([1, 3], [1, 2]), "greater")

    def test_comparisons_work_for_strings(self):
        # Strings are ordered alphabetically (by Unicode code point) - subtraction would raise TypeError.
        self.assertIs(is_greater("b", "a"), True)
        self.assertIs(is_less("apple", "banana"), True)
        self.assertIs(is_between("m", "a", "z"), True)
        self.assertEqual(max_of_three("pear", "apple", "fig"), "pear")
