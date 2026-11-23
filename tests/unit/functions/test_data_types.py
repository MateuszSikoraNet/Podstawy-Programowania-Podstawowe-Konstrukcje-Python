import unittest

from src.functions.data_types import get_type_name, is_integer, to_bool, to_float, to_int, to_str


class TestDataTypes(unittest.TestCase):
    def test_get_type_name(self):
        self.assertEqual(get_type_name(5), "int")
        self.assertEqual(get_type_name("hello"), "str")

    def test_convert_values(self):
        self.assertEqual(to_int("42"), 42)
        self.assertEqual(to_float("3.5"), 3.5)
        self.assertEqual(to_str(12), "12")

    def test_convert_to_bool(self):
        self.assertFalse(to_bool(0))
        self.assertTrue(to_bool("hello"))

    def test_is_integer(self):
        self.assertTrue(is_integer(7))
        self.assertFalse(is_integer(7.5))

    def test_invalid_numeric_conversion_raises_value_error(self):
        with self.assertRaises(ValueError):
            to_int("not a number")

    def test_to_int_of_float_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            to_int("3.5")

    def test_get_type_name_of_none_and_bool(self):
        self.assertEqual(get_type_name(None), "NoneType")
        self.assertEqual(get_type_name(True), "bool")

    def test_to_bool_of_falsy_values(self):
        for value in ("", [], None, 0.0):
            self.assertFalse(to_bool(value))

    def test_to_bool_of_nonempty_list_is_true(self):
        self.assertTrue(to_bool([0]))

    def test_is_integer_rejects_bool(self):
        # bool is a subclass of int, so isinstance(value, int) is not enough.
        self.assertFalse(is_integer(True))
        self.assertFalse(is_integer(False))

