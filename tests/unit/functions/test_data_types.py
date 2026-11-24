import unittest

from src.functions.data_types import (
    add_one,
    aliased_lists,
    append_inside_tuple,
    append_item,
    complex_parts,
    concat_str_int,
    copied_lists,
    dynamic_types,
    floor_division_type,
    from_bytes,
    get_type_name,
    int_representations,
    is_close,
    is_float,
    is_hashable,
    is_integer,
    is_nan,
    is_none,
    join_chars,
    make_range,
    make_single_tuple,
    mixed_sum_type,
    rebound_int,
    repeat,
    round_value,
    shallow_copied_nested,
    sum_of_tenths,
    to_bool,
    to_bytearray,
    to_bytes,
    to_char,
    to_code,
    to_dict,
    to_float,
    to_int,
    to_int_with_base,
    to_list,
    to_set,
    to_memoryview,
    to_str,
    to_tuple,
    true_division_type,
    truncate,
    try_add_to_frozenset,
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
        result = sum_of_tenths()
        self.assertIs(type(result), float)
        self.assertNotEqual(result, 0.3)

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

    def test_to_int_accepts_sign_whitespace_and_underscores(self):
        self.assertEqual(to_int(" -42 "), -42)
        self.assertEqual(to_int("+7"), 7)
        self.assertEqual(to_int("1_000_000"), 1000000)

    def test_to_int_with_base(self):
        self.assertEqual(to_int_with_base("ff", 16), 255)
        self.assertEqual(to_int_with_base("101", 2), 5)
        self.assertEqual(to_int_with_base("17", 8), 15)

    def test_to_int_with_base_zero_reads_the_prefix(self):
        self.assertEqual(to_int_with_base("0x1f", 0), 31)
        self.assertEqual(to_int_with_base("0b101", 0), 5)
        self.assertEqual(to_int_with_base("0o17", 0), 15)

    def test_to_int_with_digit_outside_base_raises_value_error(self):
        with self.assertRaises(ValueError):
            to_int_with_base("2", 2)

    def test_int_literals_in_other_bases_are_plain_ints(self):
        self.assertEqual(0xFF, 255)
        self.assertEqual(get_type_name(0b101), "int")

    def test_int_representations(self):
        self.assertEqual(int_representations(10), ("0b1010", "0o12", "0xa"))
        self.assertEqual(int_representations(-5), ("-0b101", "-0o5", "-0x5"))
        self.assertEqual(get_type_name(int_representations(10)[0]), "str")

    def test_to_int_of_infinity_raises_overflow_error(self):
        with self.assertRaises(OverflowError):
            to_int(float("inf"))

    def test_to_int_of_nan_raises_value_error(self):
        with self.assertRaises(ValueError):
            to_int(float("nan"))

    def test_complex_parts(self):
        self.assertEqual(complex_parts(3 + 4j), (3.0, 4.0, 3 - 4j, 5.0))
        self.assertEqual(get_type_name(complex_parts(3 + 4j)[0]), "float")

    def test_complex_arithmetic(self):
        # j * j is -1.
        self.assertEqual(mixed_sum_type(1, 2j), "complex")
        self.assertEqual(complex_parts(1j * 1j)[:2], (-1.0, 0.0))

    def test_range_is_a_lazy_immutable_sequence(self):
        numbers = make_range(0, 10, 3)
        self.assertEqual(get_type_name(numbers), "range")
        self.assertEqual(list(numbers), [0, 3, 6, 9])
        self.assertEqual(len(numbers), 4)
        self.assertEqual(numbers[-1], 9)
        with self.assertRaises(TypeError):
            numbers[0] = 1

    def test_range_excludes_stop_and_can_count_down(self):
        self.assertNotIn(10, make_range(0, 10, 1))
        self.assertEqual(list(make_range(3, 0, -1)), [3, 2, 1])
        self.assertEqual(list(make_range(0, 0, 1)), [])

    def test_range_with_zero_step_raises_value_error(self):
        with self.assertRaises(ValueError):
            make_range(0, 10, 0)

    def test_single_element_tuple_needs_a_comma(self):
        result = make_single_tuple(1)
        self.assertEqual(result, (1,))
        self.assertEqual(get_type_name(result), "tuple")
        # Parentheses alone do not make a tuple.
        self.assertEqual(get_type_name((1)), "int")

    def test_bytearray_is_mutable_bytes(self):
        data = to_bytearray("abc")
        self.assertEqual(get_type_name(data), "bytearray")
        data[0] = 65
        self.assertEqual(data, bytearray(b"Abc"))

    def test_bytes_are_immutable(self):
        data = to_bytes("abc")
        self.assertEqual(data, b"abc")
        with self.assertRaises(TypeError):
            data[0] = 65

    def test_immutable_values_are_hashable(self):
        for value in (1, 1.5, "a", None, True, (1, 2), frozenset({1}), b"a"):
            self.assertIs(is_hashable(value), True)

    def test_mutable_containers_are_not_hashable(self):
        for value in ([1], {"a": 1}, {1}, bytearray(b"a")):
            self.assertIs(is_hashable(value), False)

    def test_tuple_containing_list_is_not_hashable(self):
        self.assertIs(is_hashable((1, [2])), False)

    def test_frozenset_is_immutable(self):
        with self.assertRaises(AttributeError):
            try_add_to_frozenset(frozenset({1}), 2)

    def test_floats_should_be_compared_with_tolerance(self):
        self.assertIs(is_close(sum_of_tenths(), 0.3), True)
        self.assertIs(is_close(1.0, 1.1), False)

    def test_tuple_immutability_is_shallow(self):
        items = ([1], "x")
        result = append_inside_tuple(items, 2)
        self.assertIs(result, items)
        self.assertEqual(items, ([1, 2], "x"))

    def test_copy_creates_independent_list(self):
        # Unlike aliased_lists, a copy does not see changes made to the other list.
        self.assertEqual(copied_lists(), [1])

    def test_dynamic_typing(self):
        self.assertEqual(dynamic_types(), ("int", "str", "NoneType"))

    def test_to_bool_of_empty_and_zero_values_of_every_type(self):
        for value in (0, 0j, (), {}, set(), range(0), b"", False):
            self.assertIs(to_bool(value), False)
        for value in (-1, 0.1, (0,), {0: 0}, {0}, " ", b"\x00"):
            self.assertIs(to_bool(value), True)

    def test_set_keeps_only_unique_elements(self):
        self.assertEqual(to_set([1, 2, 2, 3, 1]), {1, 2, 3})
        self.assertEqual(to_set("hello"), {"h", "e", "l", "o"})
        self.assertEqual(get_type_name(to_set([])), "set")

    def test_set_has_no_indexing(self):
        items = to_set([1, 2])
        self.assertEqual(items, {1, 2})
        with self.assertRaises(TypeError):
            items[0]

    def test_set_elements_must_be_hashable(self):
        with self.assertRaises(TypeError):
            to_set([[1], [2]])

    def test_equal_numbers_of_different_types_are_one_set_element(self):
        # 1 == 1.0 == True and they have the same hash.
        self.assertEqual(len(to_set([1, 1.0, True])), 1)

    def test_dict_keys_are_unique_and_last_value_wins(self):
        self.assertEqual(to_dict([("a", 1), ("b", 2), ("a", 3)]), {"a": 3, "b": 2})

    def test_dict_keeps_insertion_order(self):
        self.assertEqual(list(to_dict([("z", 1), ("a", 2), ("m", 3)])), ["z", "a", "m"])

    def test_dict_keys_must_be_hashable(self):
        with self.assertRaises(TypeError):
            to_dict([([1], "list as key")])

    def test_equal_numbers_of_different_types_are_one_dict_key(self):
        self.assertEqual(to_dict([(1, "int"), (1.0, "float"), (True, "bool")]), {1: "bool"})

    def test_types_are_objects_too(self):
        self.assertEqual(get_type_name(int), "type")
        self.assertEqual(get_type_name(type(None)), "type")

    def test_get_type_name_of_float_and_list(self):
        self.assertEqual(get_type_name(1.5), "float")
        self.assertEqual(get_type_name([]), "list")

    def test_to_tuple_converts_any_iterable(self):
        self.assertEqual(to_tuple([1, 2]), (1, 2))
        self.assertEqual(to_tuple("ab"), ("a", "b"))
        self.assertEqual(get_type_name(to_tuple([])), "tuple")

    def test_memoryview_shares_the_buffer(self):
        data = to_bytearray("abc")
        view = to_memoryview(data)
        self.assertEqual(get_type_name(view), "memoryview")
        view[0] = 65
        self.assertEqual(data, bytearray(b"Abc"))

    def test_memoryview_of_bytes_is_read_only(self):
        view = to_memoryview(to_bytes("abc"))
        self.assertIs(view.readonly, True)
        with self.assertRaises(TypeError):
            view[0] = 65

    def test_rebinding_immutable_int_does_not_change_alias(self):
        # Unlike aliased_lists, += on an int creates a new object.
        self.assertEqual(rebound_int(), 5)

    def test_copy_is_shallow(self):
        # The copy is a new list, but the inner list is still shared.
        self.assertEqual(shallow_copied_nested(), [[1, 2]])

    def test_float_loses_precision_for_big_ints(self):
        # float has 53 bits of precision, int is exact.
        self.assertEqual(to_float(2 ** 53 + 1), 2 ** 53)
        self.assertNotEqual(add_one(2 ** 53), 2 ** 53)

    def test_get_type_name_of_builtin_singletons(self):
        self.assertEqual(get_type_name(...), "ellipsis")
        self.assertEqual(get_type_name(NotImplemented), "NotImplementedType")

    def test_to_str_of_a_string_is_unchanged(self):
        # str() gives the readable text; repr() would add quotes.
        self.assertEqual(to_str("hi"), "hi")
        self.assertEqual(to_str(0.5), "0.5")

    def test_whole_float_is_not_an_integer(self):
        # 7.0 has no fraction, but its type is still float.
        self.assertIs(is_integer(7.0), False)
        self.assertIs(is_float(7.0), True)

    def test_bytearray_uses_utf8(self):
        self.assertEqual(to_bytearray("ż"), bytearray(b"\xc5\xbc"))
