import unittest

from src.functions.data_types import (
    add_one,
    aliased_lists,
    append_item,
    concat_str_int,
    floor_division_type,
    from_bytes,
    get_type_name,
    is_float,
    is_integer,
    is_nan,
    is_none,
    join_chars,
    mixed_sum_type,
    repeat,
    round_value,
    sum_of_tenths,
    to_bool,
    to_bytes,
    to_char,
    to_code,
    to_float,
    to_int,
    to_list,
    to_str,
    true_division_type,
    truncate,
    try_assign_string_index,
    try_assign_tuple_index,
)


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
            self.assertIs(to_bool(value), False)

    def test_to_bool_of_nonempty_list_is_true(self):
        self.assertIs(to_bool([0]), True)

    def test_is_integer_rejects_bool(self):
        # bool is a subclass of int, so isinstance(value, int) is not enough.
        self.assertIs(is_integer(True), False)
        self.assertIs(is_integer(False), False)

    def test_is_float(self):
        self.assertIs(is_float(7.5), True)
        self.assertIs(is_float(7), False)
        self.assertIs(is_float(True), False)

    def test_to_int_of_bool(self):
        # bool is a subclass of int, so int(True) is 1.
        self.assertEqual(to_int(True), 1)
        self.assertEqual(to_int(False), 0)

    def test_to_str_of_bool(self):
        self.assertEqual(to_str(True), "True")

    def test_to_float_from_int_returns_float(self):
        result = to_float(3)
        self.assertEqual(result, 3.0)
        self.assertIs(type(result), float)

    def test_true_division_always_returns_float(self):
        self.assertEqual(true_division_type(10, 2), "float")

    def test_floor_division_type_depends_on_operands(self):
        self.assertEqual(floor_division_type(10, 4), "int")
        self.assertEqual(floor_division_type(10.0, 4), "float")

    def test_truncate_goes_toward_zero_not_rounding(self):
        self.assertEqual(truncate(3.9), 3)
        self.assertEqual(truncate(-3.9), -3)

    def test_float_addition_is_not_exact(self):
        # 0.1 + 0.2 is not 0.3 in binary floating point.
        self.assertNotEqual(sum_of_tenths(), 0.3)

    def test_repeat_string(self):
        self.assertEqual(repeat("ab", 3), "ababab")

    def test_repeat_with_float_times_raises_type_error(self):
        with self.assertRaises(TypeError):
            repeat("ab", 2.5)

    def test_to_bytes_returns_bytes(self):
        self.assertEqual(to_bytes("abc"), b"abc")
        self.assertEqual(get_type_name(to_bytes("abc")), "bytes")

    def test_is_none_only_for_none(self):
        # None is falsy but falsy is not None.
        self.assertIs(is_none(None), True)
        for value in (0, "", [], False):
            self.assertIs(is_none(value), False)

    def test_add_one_of_big_number_stays_exact(self):
        # Python ints have arbitrary precision, no overflow.
        self.assertEqual(add_one(10 ** 20), 10 ** 20 + 1)

    def test_lists_are_mutable_in_place(self):
        items = [1, 2]
        result = append_item(items, 3)
        self.assertIsNone(result)
        self.assertEqual(items, [1, 2, 3])

    def test_strings_are_immutable(self):
        with self.assertRaises(TypeError):
            try_assign_string_index("hello")

    def test_tuples_are_immutable(self):
        with self.assertRaises(TypeError):
            try_assign_tuple_index((1, 2, 3))

    def test_get_type_name_of_complex(self):
        self.assertEqual(get_type_name(1j), "complex")

    def test_to_bool_of_string_false_is_true(self):
        # "False" is a non-empty string, so it is truthy.
        self.assertIs(to_bool("False"), True)

    def test_to_str_of_none(self):
        self.assertEqual(to_str(None), "None")

    def test_to_int_of_none_raises_type_error(self):
        # None cannot be converted at all - TypeError, not ValueError.
        with self.assertRaises(TypeError):
            to_int(None)

    def test_to_float_of_scientific_notation_string(self):
        self.assertEqual(to_float("1e3"), 1000.0)

    def test_to_float_of_bool(self):
        result = to_float(True)
        self.assertEqual(result, 1.0)
        self.assertIs(type(result), float)

    def test_to_char_and_to_code(self):
        self.assertEqual(to_char(65), "A")
        self.assertEqual(to_code("A"), 65)

    def test_to_list_splits_string_into_chars(self):
        self.assertEqual(to_list("abc"), ["a", "b", "c"])

    def test_join_chars_builds_string(self):
        self.assertEqual(join_chars(["a", "b", "c"]), "abc")

    def test_round_of_halves_goes_to_even(self):
        # round() uses banker's rounding, not "round half up".
        self.assertEqual(round_value(2.5), 2)
        self.assertEqual(round_value(3.5), 4)

    def test_mixed_int_float_sum_is_float(self):
        self.assertEqual(mixed_sum_type(1, 2.0), "float")
        self.assertEqual(mixed_sum_type(1, 2), "int")

    def test_is_nan_only_for_nan(self):
        self.assertIs(is_nan(float("nan")), True)
        self.assertIs(is_nan(0.0), False)
        self.assertIs(is_nan(None), False)

    def test_to_int_of_float_truncates_toward_zero(self):
        # int() on a float truncates, it does not round.
        self.assertEqual(to_int(3.9), 3)
        self.assertEqual(to_int(-3.9), -3)

    def test_to_float_of_invalid_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            to_float("abc")

    def test_to_float_of_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            to_float(None)

    def test_concat_str_int_raises_type_error(self):
        # Python does not convert int to str implicitly.
        with self.assertRaises(TypeError):
            concat_str_int("a", 1)

    def test_from_bytes_round_trip_with_non_ascii(self):
        # "ż" takes 2 bytes in utf-8; encode and decode must round-trip.
        data = to_bytes("ż")
        self.assertEqual(data, b"\xc5\xbc")
        self.assertEqual(len(data), 2)
        self.assertEqual(from_bytes(data), "ż")

    def test_aliased_names_share_one_mutable_object(self):
        # b = a does not copy - both names refer to the same list.
        self.assertEqual(aliased_lists(), [1, 2])

    def test_bytes_indexing_returns_int_not_str(self):
        # bytes is a sequence of integers, not of one-character strings.
        data = to_bytes("abc")
        self.assertEqual(data[0], 97)
        self.assertEqual(get_type_name(data[0]), "int")

    def test_to_char_of_invalid_code_raises_value_error(self):
        with self.assertRaises(ValueError):
            to_char(0x110000)

    def test_to_code_of_multichar_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            to_code("AB")

    def test_to_float_of_huge_int_raises_overflow_error(self):
        # int has no range limit, float does.
        with self.assertRaises(OverflowError):
            to_float(10 ** 400)

    def test_to_float_of_infinity(self):
        result = to_float("inf")
        self.assertIs(type(result), float)
        self.assertGreater(result, 10 ** 1000)

    def test_get_type_name_of_dict_set_frozenset(self):
        self.assertEqual(get_type_name({}), "dict")
        self.assertEqual(get_type_name(set()), "set")
        self.assertEqual(get_type_name(frozenset()), "frozenset")

    def test_bool_arithmetic_is_int(self):
        # bool is a subclass of int, so True + True is the int 2.
        self.assertEqual(mixed_sum_type(True, True), "int")

    def test_repeat_zero_or_negative_times_is_empty(self):
        self.assertEqual(repeat("ab", 0), "")
        self.assertEqual(repeat("ab", -1), "")

