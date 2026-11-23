import unittest

from src.objects.data_types import TypeConverter


class TestTypeConverter(unittest.TestCase):
    def setUp(self):
        self.converter = TypeConverter()

    def test_get_type_name(self):
        self.assertEqual(self.converter.get_type_name(5), "int")
        self.assertEqual(self.converter.get_type_name("hello"), "str")

    def test_convert_values(self):
        self.assertEqual(self.converter.to_int("42"), 42)
        self.assertEqual(self.converter.to_float("3.5"), 3.5)
        self.assertEqual(self.converter.to_str(12), "12")

    def test_convert_to_bool(self):
        self.assertFalse(self.converter.to_bool(0))
        self.assertTrue(self.converter.to_bool("hello"))

    def test_is_integer(self):
        self.assertTrue(self.converter.is_integer(7))
        self.assertFalse(self.converter.is_integer(7.5))

    def test_invalid_numeric_conversion_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.converter.to_int("not a number")

    def test_to_int_of_float_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.converter.to_int("3.5")

    def test_get_type_name_of_none_and_bool(self):
        self.assertEqual(self.converter.get_type_name(None), "NoneType")
        self.assertEqual(self.converter.get_type_name(True), "bool")

    def test_to_bool_of_falsy_values(self):
        for value in ("", [], None, 0.0):
            self.assertIs(self.converter.to_bool(value), False)

    def test_to_bool_of_nonempty_list_is_true(self):
        self.assertIs(self.converter.to_bool([0]), True)

    def test_is_integer_rejects_bool(self):
        # bool is a subclass of int, so isinstance(value, int) is not enough.
        self.assertIs(self.converter.is_integer(True), False)
        self.assertIs(self.converter.is_integer(False), False)

    def test_is_float(self):
        self.assertIs(self.converter.is_float(7.5), True)
        self.assertIs(self.converter.is_float(7), False)
        self.assertIs(self.converter.is_float(True), False)

    def test_to_int_of_bool(self):
        # bool is a subclass of int, so int(True) is 1.
        self.assertEqual(self.converter.to_int(True), 1)
        self.assertEqual(self.converter.to_int(False), 0)

    def test_to_str_of_bool(self):
        self.assertEqual(self.converter.to_str(True), "True")

    def test_to_float_from_int_returns_float(self):
        result = self.converter.to_float(3)
        self.assertEqual(result, 3.0)
        self.assertIs(type(result), float)

    def test_true_division_always_returns_float(self):
        self.assertEqual(self.converter.true_division_type(10, 2), "float")

    def test_floor_division_type_depends_on_operands(self):
        self.assertEqual(self.converter.floor_division_type(10, 4), "int")
        self.assertEqual(self.converter.floor_division_type(10.0, 4), "float")

    def test_truncate_goes_toward_zero_not_rounding(self):
        self.assertEqual(self.converter.truncate(3.9), 3)
        self.assertEqual(self.converter.truncate(-3.9), -3)

    def test_float_addition_is_not_exact(self):
        # 0.1 + 0.2 is not 0.3 in binary floating point.
        self.assertNotEqual(self.converter.sum_of_tenths(), 0.3)

    def test_repeat_string(self):
        self.assertEqual(self.converter.repeat("ab", 3), "ababab")

    def test_repeat_with_float_times_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.converter.repeat("ab", 2.5)

    def test_to_bytes_returns_bytes(self):
        self.assertEqual(self.converter.to_bytes("abc"), b"abc")
        self.assertEqual(self.converter.get_type_name(self.converter.to_bytes("abc")), "bytes")

    def test_is_none_only_for_none(self):
        # None is falsy but falsy is not None.
        self.assertIs(self.converter.is_none(None), True)
        for value in (0, "", [], False):
            self.assertIs(self.converter.is_none(value), False)

    def test_add_one_of_big_number_stays_exact(self):
        # Python ints have arbitrary precision, no overflow.
        self.assertEqual(self.converter.add_one(10 ** 20), 10 ** 20 + 1)

    def test_lists_are_mutable_in_place(self):
        items = [1, 2]
        result = self.converter.append_item(items, 3)
        self.assertIsNone(result)
        self.assertEqual(items, [1, 2, 3])

    def test_strings_are_immutable(self):
        with self.assertRaises(TypeError):
            self.converter.try_assign_string_index("hello")

    def test_tuples_are_immutable(self):
        with self.assertRaises(TypeError):
            self.converter.try_assign_tuple_index((1, 2, 3))

    def test_get_type_name_of_complex(self):
        self.assertEqual(self.converter.get_type_name(1j), "complex")

    def test_to_bool_of_string_false_is_true(self):
        # "False" is a non-empty string, so it is truthy.
        self.assertIs(self.converter.to_bool("False"), True)

    def test_to_str_of_none(self):
        self.assertEqual(self.converter.to_str(None), "None")

    def test_to_int_of_none_raises_type_error(self):
        # None cannot be converted at all - TypeError, not ValueError.
        with self.assertRaises(TypeError):
            self.converter.to_int(None)

    def test_to_float_of_scientific_notation_string(self):
        self.assertEqual(self.converter.to_float("1e3"), 1000.0)

    def test_to_float_of_bool(self):
        result = self.converter.to_float(True)
        self.assertEqual(result, 1.0)
        self.assertIs(type(result), float)

    def test_to_char_and_to_code(self):
        self.assertEqual(self.converter.to_char(65), "A")
        self.assertEqual(self.converter.to_code("A"), 65)

    def test_to_list_splits_string_into_chars(self):
        self.assertEqual(self.converter.to_list("abc"), ["a", "b", "c"])

    def test_join_chars_builds_string(self):
        self.assertEqual(self.converter.join_chars(["a", "b", "c"]), "abc")

    def test_round_of_halves_goes_to_even(self):
        # round() uses banker's rounding, not "round half up".
        self.assertEqual(self.converter.round_value(2.5), 2)
        self.assertEqual(self.converter.round_value(3.5), 4)

    def test_mixed_int_float_sum_is_float(self):
        self.assertEqual(self.converter.mixed_sum_type(1, 2.0), "float")
        self.assertEqual(self.converter.mixed_sum_type(1, 2), "int")

    def test_is_nan_only_for_nan(self):
        self.assertIs(self.converter.is_nan(float("nan")), True)
        self.assertIs(self.converter.is_nan(0.0), False)
        self.assertIs(self.converter.is_nan(None), False)

