import unittest

from src.functions.lists_dicts_tuples import (
    count_occurrences,
    create_dict,
    get_first_and_last,
    get_value_or_default,
    list_to_tuple,
    merge_dicts,
    sorted_keys,
    tuple_to_list,
)


class TestListsDictsTuples(unittest.TestCase):
    def test_create_dict(self):
        self.assertEqual(create_dict(["a", "b"], [1, 2]), {"a": 1, "b": 2})
        self.assertEqual(create_dict(["a", "b"], [1]), {"a": 1})

    def test_get_first_and_last(self):
        self.assertEqual(get_first_and_last([1, 2, 3]), (1, 3))
        self.assertEqual(get_first_and_last([4]), (4, 4))
        with self.assertRaises(ValueError):
            get_first_and_last([])

    def test_convert_list_and_tuple(self):
        self.assertEqual(list_to_tuple([1, 2]), (1, 2))
        self.assertEqual(tuple_to_list((1, 2)), [1, 2])

    def test_dictionary_and_collection_operations(self):
        self.assertEqual(count_occurrences([1, 2, 1], 1), 2)
        self.assertEqual(get_value_or_default({"a": 1}, "b", 0), 0)
        self.assertEqual(merge_dicts({"a": 1}, {"a": 2, "b": 3}), {"a": 2, "b": 3})
        self.assertEqual(sorted_keys({"b": 2, "a": 1}), ["a", "b"])

    def test_create_dict_stops_at_the_shorter_list(self):
        self.assertEqual(create_dict(["a"], [1, 2]), {"a": 1})
        self.assertEqual(create_dict([], []), {})

    def test_get_value_or_default_returns_existing_values(self):
        # An existing falsy value (0) is a real value, not a missing key.
        self.assertEqual(get_value_or_default({"a": 0}, "a", 5), 0)
        self.assertEqual(get_value_or_default({"a": "x"}, "a"), "x")
        self.assertIsNone(get_value_or_default({}, "a"))

    def test_merge_dicts_does_not_change_the_inputs(self):
        first, second = {"a": 1}, {"b": 2}
        self.assertEqual(merge_dicts(first, second), {"a": 1, "b": 2})
        self.assertEqual(first, {"a": 1})
        self.assertEqual(second, {"b": 2})

    def test_sorted_keys_sorts_keys_not_values(self):
        self.assertEqual(sorted_keys({"b": 1, "a": 2, "c": 0}), ["a", "b", "c"])
