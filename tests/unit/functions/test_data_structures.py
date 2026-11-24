import unittest

from src.functions.data_structures import (
    any_all_negative,
    copy_and_clear,
    count_by_cell,
    describe_point,
    dict_views,
    edit_dict,
    edit_list,
    edit_set,
    edit_slices,
    empty_groups,
    frequencies,
    get_path,
    group_by_length,
    head_and_tail,
    keys_by_value,
    longest_word,
    names_sorted_by_age,
    pop_first_and_clear,
    pop_key,
    remove_negatives_in_place,
    remove_zero_values,
    run_queue,
    run_stack,
    slices,
    sort_and_reverse,
    sort_pair,
    summarize,
    tuple_methods,
)


class TestDataStructures(unittest.TestCase):
    def test_slicing(self):
        values = [10, 20, 30, 40, 50]
        self.assertEqual(slices(values), ([20, 30], [40, 50], [10, 30, 50], [50, 40, 30, 20, 10]))
        self.assertEqual(values, [10, 20, 30, 40, 50])
        self.assertEqual(slices("abcde"), ("bc", "de", "ace", "edcba"))
        # Slices never raise IndexError, they just get shorter.
        self.assertEqual(slices([1]), ([], [1], [1], [1]))

    def test_list_methods_change_the_list_in_place(self):
        values = [1, 2, 3]
        self.assertEqual(edit_list(values), 6)
        self.assertEqual(values, [0, 1, 3, 4, 5])

    def test_list_remove_of_missing_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            edit_list([1, 3])

    def test_stack_is_last_in_first_out(self):
        operations = [("push", 1), ("push", 2), ("pop",), ("push", 3), ("pop",), ("pop",)]
        self.assertEqual(run_stack(operations), [2, 3, 1])
        self.assertEqual(run_stack([]), [])
        with self.assertRaises(IndexError):
            run_stack([("push", 1), ("pop",), ("pop",)])

    def test_queue_is_first_in_first_out(self):
        operations = [("push", 1), ("push", 2), ("pop",), ("push", 3), ("pop",), ("pop",)]
        self.assertEqual(run_queue(operations), [1, 2, 3])
        with self.assertRaises(IndexError):
            run_queue([("pop",)])

    def test_pop_key_removes_and_returns(self):
        mapping = {"a": 1, "b": 2}
        self.assertEqual(pop_key(mapping, "a"), 1)
        self.assertEqual(mapping, {"b": 2})

    def test_missing_key_raises_key_error(self):
        mapping = {"a": 1}
        with self.assertRaises(KeyError):
            pop_key(mapping, "z")
        self.assertEqual(mapping, {"a": 1})

    def test_dict_views(self):
        self.assertEqual(dict_views({"b": 2, "a": 1}), (["b", "a"], [2, 1], [("b", 2), ("a", 1)]))
        self.assertEqual(dict_views({}), ([], [], []))

    def test_set_methods(self):
        items = {1, 2}
        self.assertIsNone(edit_set(items))
        self.assertEqual(items, {2, 4})

    def test_set_remove_of_missing_value_raises_key_error(self):
        with self.assertRaises(KeyError):
            edit_set({2})

    def test_star_unpacking(self):
        self.assertEqual(head_and_tail([1, 2, 3]), (1, [2, 3]))
        self.assertEqual(head_and_tail((7,)), (7, []))
        self.assertEqual(head_and_tail("abc"), ("a", ["b", "c"]))
        with self.assertRaises(ValueError):
            head_and_tail([])

    def test_frequencies(self):
        result = frequencies(["b", "a", "b", "c", "b"])
        self.assertEqual(result, {"b": 3, "a": 1, "c": 1})
        self.assertEqual(list(result), ["b", "a", "c"])
        self.assertEqual(frequencies([]), {})

    def test_group_by_length_builds_dict_of_lists(self):
        result = group_by_length(["dog", "horse", "cat", "ox"])
        self.assertEqual(result, {3: ["dog", "cat"], 5: ["horse"], 2: ["ox"]})
        self.assertEqual(list(result), [3, 5, 2])
        self.assertEqual(group_by_length([]), {})

    def test_list_of_dicts_sorted_by_field(self):
        people = [
            {"name": "Cy", "age": 36},
            {"name": "Bob", "age": 25},
            {"name": "Ada", "age": 36},
            {"name": "Di", "age": 19},
            {"name": "Eve", "age": 36},
        ]
        # Cy, Ada and Eve are all 36 - they keep their original order (neither A-Z nor Z-A).
        self.assertEqual(names_sorted_by_age(people), ["Di", "Bob", "Cy", "Ada", "Eve"])
        self.assertEqual([p["name"] for p in people], ["Cy", "Bob", "Ada", "Di", "Eve"])

    def test_remove_deletes_only_the_first_occurrence(self):
        values = [2, 1, 2]
        self.assertEqual(edit_list(values), 6)
        self.assertEqual(values, [0, 1, 2, 4, 5])

    def test_sort_and_reverse_return_none(self):
        values = [3, 1, 2]
        self.assertEqual(sort_and_reverse(values), (None, None))
        self.assertEqual(values, [3, 2, 1])

    def test_slice_assignment_and_del(self):
        values = [1, 2, 3, 4, 5]
        alias = values
        self.assertIsNone(edit_slices(values))
        self.assertEqual(values, ["a", "b", "c"])
        self.assertIs(alias, values)

    def test_remove_while_iterating_pitfall(self):
        # Two negatives in a row: removing inside "for v in values" would skip -2.
        values = [-1, -2, 3, -4, -5, 0, 6]
        alias = values
        self.assertIsNone(remove_negatives_in_place(values))
        # 0 is not negative, so it stays.
        self.assertEqual(values, [3, 0, 6])
        self.assertEqual(alias, [3, 0, 6])
        empty = []
        remove_negatives_in_place(empty)
        self.assertEqual(empty, [])

    def test_pop_with_index_and_clear(self):
        values = [7, 8, 9]
        alias = values
        self.assertEqual(pop_first_and_clear(values), 7)
        self.assertEqual(values, [])
        self.assertIs(alias, values)
        with self.assertRaises(IndexError):
            pop_first_and_clear([])

    def test_dict_methods_change_the_dict_in_place(self):
        mapping = {"a": 0, "z": 9}
        self.assertEqual(edit_dict(mapping), ("d", 4))
        self.assertEqual(mapping, {"a": 1, "z": 9, "b": 2})
        # Overwriting "a" kept its first position.
        self.assertEqual(list(mapping), ["a", "z", "b"])

    def test_edit_dict_on_empty_dict(self):
        mapping = {}
        self.assertEqual(edit_dict(mapping), ("d", 4))
        self.assertEqual(list(mapping.items()), [("a", 1), ("b", 2)])

    def test_each_key_gets_its_own_list(self):
        groups = empty_groups(["x", "y"])
        self.assertEqual(groups, {"x": [], "y": []})
        groups["x"].append(1)
        self.assertEqual(groups["y"], [])
        self.assertEqual(empty_groups([]), {})

    def test_delete_keys_without_changing_dict_size_during_iteration(self):
        mapping = {"a": 0, "b": 1, "c": 0, "d": 2}
        alias = mapping
        self.assertIsNone(remove_zero_values(mapping))
        self.assertEqual(alias, {"b": 1, "d": 2})
        self.assertIs(alias, mapping)

    def test_keys_sorted_by_value(self):
        scores = {"Bob": 70, "Ann": 90, "Cy": 85, "Di": 90, "Ed": 70}
        # Ann and Di tie (90), Bob and Ed tie (70) - ties keep dict order.
        self.assertEqual(keys_by_value(scores), ["Ann", "Di", "Cy", "Bob", "Ed"])
        self.assertEqual(keys_by_value({}), [])

    def test_nested_dict_access(self):
        data = {"user": {"address": {"city": "Kraków"}, "age": 0}}
        self.assertEqual(get_path(data, ["user", "address", "city"]), "Kraków")
        self.assertEqual(get_path(data, ["user", "age"]), 0)
        self.assertEqual(get_path(data, ["user", "address"]), {"city": "Kraków"})
        self.assertIsNone(get_path(data, ["user", "phone"]))
        self.assertEqual(get_path(data, ["user", "age", "x"], "n/a"), "n/a")
        self.assertEqual(get_path(data, [], "n/a"), data)

    def test_dict_copy_is_shallow_and_clear_empties_in_place(self):
        inner = [1]
        mapping = {"a": inner, "b": 2}
        alias = mapping
        backup = copy_and_clear(mapping)
        self.assertEqual(alias, {})
        self.assertEqual(backup, {"a": [1], "b": 2})
        self.assertIsNot(backup, mapping)
        # Shallow copy: the nested list is the same object.
        self.assertIs(backup["a"], inner)

    def test_tuple_methods(self):
        self.assertEqual(tuple_methods((3, 1, 3, 2), 3), (2, 0))
        self.assertEqual(tuple_methods(("a", "b"), "b"), (1, 1))
        with self.assertRaises(ValueError):
            tuple_methods((1, 2), 9)

    def test_swap_with_tuple_unpacking(self):
        self.assertEqual(sort_pair(5, 2), (2, 5))
        self.assertEqual(sort_pair(2, 5), (2, 5))
        self.assertEqual(sort_pair(4, 4), (4, 4))
        self.assertIsInstance(sort_pair(1, 2), tuple)

    def test_nested_unpacking(self):
        self.assertEqual(describe_point(((1, 2), "A")), "A at 1,2")
        self.assertEqual(describe_point(([3, 4], "B")), "B at 3,4")

    def test_unpacking_wrong_number_of_values_raises_value_error(self):
        with self.assertRaises(ValueError):
            describe_point(((1, 2, 3), "A"))  # too many values
        with self.assertRaises(ValueError):
            describe_point(((1,), "A"))  # not enough values

    def test_tuples_as_dict_keys(self):
        result = count_by_cell([(0, 0), (1, 2), (0, 0)])
        self.assertEqual(result, {(0, 0): 2, (1, 2): 1})
        self.assertEqual(count_by_cell([]), {})

    def test_slicing_a_tuple_gives_a_tuple(self):
        self.assertEqual(slices((10, 20, 30, 40, 50)), ((20, 30), (40, 50), (10, 30, 50), (50, 40, 30, 20, 10)))

    def test_same_operations_work_on_every_collection(self):
        self.assertEqual(summarize([3, 1, 2]), (3, 1, 3, [1, 2, 3]))
        # A list keeps duplicates - only the set below removes them.
        self.assertEqual(summarize([3, 1, 3]), (3, 1, 3, [1, 3, 3]))
        self.assertEqual(summarize((3, 1, 2)), (3, 1, 3, [1, 2, 3]))
        self.assertEqual(summarize({3, 1, 2, 3}), (3, 1, 3, [1, 2, 3]))
        self.assertEqual(summarize("cab"), (3, "a", "c", ["a", "b", "c"]))
        # A dict is a collection of its keys.
        self.assertEqual(summarize({"b": 9, "a": 0}), (2, "a", "b", ["a", "b"]))

    def test_any_and_all(self):
        self.assertEqual(any_all_negative([-1, 2]), (True, False))
        self.assertEqual(any_all_negative([-1, -2]), (True, True))
        self.assertEqual(any_all_negative([0, 1]), (False, False))
        # 0 is not negative.
        self.assertEqual(any_all_negative([-1, 0]), (True, False))
        self.assertEqual(any_all_negative(()), (False, True))

    def test_max_with_key(self):
        self.assertEqual(longest_word(["ab", "abcd", "xyzw", "a"]), "abcd")
        self.assertEqual(longest_word(["zz", "a"]), "zz")
        with self.assertRaises(ValueError):
            longest_word([])
