import unittest

from src.functions.variables import (
    accumulate,
    chained_assignment,
    decrement,
    delete_variable,
    get_default_values,
    increment,
    is_valid_name,
    swap,
)


class TestVariables(unittest.TestCase):
    def test_swap(self):
        self.assertEqual(swap("left", "right"), ("right", "left"))

    def test_increment_and_decrement(self):
        self.assertEqual(increment(4), 5)
        self.assertEqual(increment(4, 3), 7)
        self.assertEqual(decrement(4), 3)
        self.assertEqual(decrement(4, 2), 2)

    def test_accumulate(self):
        self.assertEqual(accumulate([1, 2, 3]), 6)
        self.assertEqual(accumulate([]), 0)

    def test_get_default_values(self):
        self.assertEqual(get_default_values(), {"name": "", "age": 0, "active": False})

    def test_swap_numbers_and_mixed_types(self):
        self.assertEqual(swap(1, 2), (2, 1))
        self.assertEqual(swap(0, None), (None, 0))

    def test_accumulate_floats(self):
        self.assertEqual(accumulate([0.5, 0.25]), 0.75)
        self.assertEqual(accumulate([-1, 1]), 0)

    def test_get_default_values_types(self):
        defaults = get_default_values()
        self.assertIs(defaults["active"], False)
        self.assertIs(type(defaults["age"]), int)

    def test_chained_assignment_shares_one_object(self):
        self.assertEqual(chained_assignment(), [1])

    def test_valid_variable_names(self):
        for name in ("age", "_private", "total2", "MAX_SIZE", "zażółć"):
            self.assertIs(is_valid_name(name), True)
        for name in ("2total", "my-var", "my var", "", "class", "for", "None"):
            self.assertIs(is_valid_name(name), False)

    def test_deleted_variable_no_longer_exists(self):
        with self.assertRaises(NameError):
            delete_variable()

    def test_soft_keywords_and_builtin_names_are_valid_names(self):
        # match, case, _ and type are keywords only in some places, so "match = 1" works.
        # Built-in names like print can be reused too (possible, but it hides the built-in).
        for name in ("match", "case", "_", "type", "print"):
            self.assertIs(is_valid_name(name), True)
