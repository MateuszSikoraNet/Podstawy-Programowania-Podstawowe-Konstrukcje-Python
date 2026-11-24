import unittest

from src.functions.operators import (
    associativity,
    augmented_assign,
    bitwise_and,
    bitwise_not,
    bitwise_or,
    bitwise_precedence,
    bitwise_xor,
    compare_all,
    concatenate,
    divide,
    divide_with_remainder,
    extend_in_place,
    floor_divide,
    guarded_divide,
    is_even,
    is_member,
    is_not_member,
    is_not_same_object,
    is_odd,
    is_same_object,
    is_strictly_ascending,
    is_zero_or_divides,
    logical_and,
    logical_not,
    logical_or,
    logical_precedence,
    matmul,
    merge_dicts,
    modulo,
    parity_label,
    percent_format,
    power,
    precedence,
    repeat_sequence,
    set_operations,
    shift_left,
    shift_right,
    squares_above,
    unary_operators,
    value_or_default,
)


class Vector:
    # Minimal class with its own @ operator, used by the matmul tests.
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y

class TestOperators(unittest.TestCase):
    def test_arithmetic_operators(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(floor_divide(10, 3), 3)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(divide_with_remainder(10, 3), (3, 1))

    def test_even_and_odd(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(4))
        # "Check if" means a real bool, not 0/1.
        self.assertIs(is_even(4), True)
        self.assertIs(is_even(3), False)
        self.assertIs(is_odd(3), True)
        self.assertIs(is_odd(4), False)

    def test_logical_operators(self):
        self.assertFalse(logical_and(True, False))
        self.assertTrue(logical_or(False, True))
        self.assertFalse(logical_not(True))

    def test_division_by_zero_raises_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            floor_divide(10, 0)

    def test_true_division_returns_float(self):
        result = divide(10, 4)
        self.assertEqual(result, 2.5)
        self.assertIs(type(result), float)
        self.assertIs(type(divide(10, 2)), float)
        self.assertEqual(divide(1, 3), 1 / 3)

    def test_true_division_by_zero_raises_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_modulo_by_zero_raises_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)

    def test_divmod_by_zero_raises_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide_with_remainder(10, 0)

    def test_floor_division_with_negatives_rounds_down(self):
        # // rounds toward minus infinity, not toward zero.
        self.assertEqual(floor_divide(-7, 2), -4)
        self.assertEqual(floor_divide(7, -2), -4)

    def test_modulo_sign_follows_the_divisor(self):
        self.assertEqual(modulo(-7, 2), 1)
        self.assertEqual(modulo(7, -2), -1)

    def test_divmod_with_negative_dividend(self):
        self.assertEqual(divide_with_remainder(-10, 3), (-4, 2))

    def test_floor_div_and_modulo_reconstruct_the_dividend(self):
        # b * (a // b) + a % b == a for every sign combination.
        for a, b in ((10, 3), (-10, 3), (7, -2), (-7, -2)):
            self.assertEqual(b * floor_divide(a, b) + modulo(a, b), a)

    def test_power_with_negative_exponent_returns_float(self):
        result = power(2, -1)
        self.assertEqual(result, 0.5)
        self.assertIs(type(result), float)

    def test_power_with_fractional_exponent(self):
        self.assertEqual(power(4, 0.5), 2.0)

    def test_power_zero_to_zero_is_one(self):
        self.assertEqual(power(0, 0), 1)

    def test_operator_precedence(self):
        # * before +, ** before unary minus.
        self.assertEqual(precedence(), (14, 20, -4, 18))

    def test_and_or_return_operands_not_booleans(self):
        # and/or return the operand that decides the result, not True/False.
        self.assertEqual(logical_and(2, 3), 3)
        self.assertEqual(logical_and(0, 5), 0)
        self.assertEqual(logical_or(0, 5), 5)
        self.assertEqual(logical_or("", "x"), "x")

    def test_not_always_returns_bool(self):
        self.assertIs(logical_not(0), True)
        self.assertIs(logical_not("x"), False)
        self.assertIs(logical_not([]), True)

    def test_and_short_circuits_before_division(self):
        # a is 0, so "a != 0 and b / a" never evaluates b / a - no ZeroDivisionError.
        self.assertIs(guarded_divide(0, 5), False)
        self.assertEqual(guarded_divide(2, 10), 5.0)
        self.assertEqual(guarded_divide(4, 2), 0.5)

    def test_even_and_odd_for_negative_numbers(self):
        self.assertTrue(is_even(-4))
        self.assertTrue(is_odd(-3))

    def test_identity_operator_distinguishes_same_object_from_equal(self):
        # is compares object identity, not value (value equality is the comparisons module).
        items = [1, 2]
        alias = items
        self.assertIs(is_same_object(alias, items), True)
        self.assertIs(is_same_object([1, 2], [1, 2]), False)
        self.assertIs(is_same_object(None, None), True)

    def test_membership_operator_works_on_containers(self):
        self.assertIs(is_member([1, 2, 3], 2), True)
        self.assertIs(is_member([1, 2], 5), False)
        self.assertIs(is_member("hello", "ell"), True)
        # For a dict, "in" checks keys, not values.
        self.assertIs(is_member({"a": 1}, "a"), True)
        self.assertIs(is_member({"a": 1}, 1), False)

    def test_identity_negation_is_not(self):
        items = [1, 2]
        self.assertIs(is_not_same_object(items, items), False)
        self.assertIs(is_not_same_object([1, 2], [1, 2]), True)
        self.assertIs(is_not_same_object(0, None), True)

    def test_membership_negation_not_in(self):
        self.assertIs(is_not_member([1, 2, 3], 5), True)
        self.assertIs(is_not_member([1, 2, 3], 2), False)
        self.assertIs(is_not_member("hello", "xyz"), True)
        self.assertIs(is_not_member({"a": 1}, 1), True)

    def test_bitwise_and_or_xor(self):
        # 6 = 0b110, 3 = 0b011
        self.assertEqual(bitwise_and(6, 3), 2)
        self.assertEqual(bitwise_or(6, 3), 7)
        self.assertEqual(bitwise_xor(6, 3), 5)
        self.assertEqual(bitwise_xor(5, 5), 0)

    def test_bitwise_and_differs_from_logical_and(self):
        # & combines bits, "and" returns one of the operands.
        self.assertEqual(bitwise_and(6, 3), 2)
        self.assertEqual(logical_and(6, 3), 3)
        self.assertIs(bitwise_and(True, False), False)
        self.assertIs(bitwise_or(True, False), True)

    def test_bitwise_not_is_minus_x_minus_one(self):
        self.assertEqual(bitwise_not(5), -6)
        self.assertEqual(bitwise_not(0), -1)
        self.assertEqual(bitwise_not(-1), 0)

    def test_shift_operators(self):
        self.assertEqual(shift_left(1, 3), 8)
        self.assertEqual(shift_left(5, 1), 10)
        self.assertEqual(shift_right(16, 2), 4)
        self.assertEqual(shift_right(5, 1), 2)

    def test_shift_right_of_negative_rounds_down(self):
        # >> behaves like // 2 ** bits, so it rounds toward minus infinity.
        self.assertEqual(shift_right(-5, 1), -3)
        self.assertEqual(shift_right(-1, 10), -1)

    def test_negative_shift_count_raises_value_error(self):
        with self.assertRaises(ValueError):
            shift_left(1, -1)
        with self.assertRaises(ValueError):
            shift_right(1, -1)

    def test_all_comparison_operators(self):
        # (==, !=, <, <=, >, >=)
        self.assertEqual(compare_all(2, 3), (False, True, True, True, False, False))
        self.assertEqual(compare_all(3, 3), (True, False, False, True, False, True))
        self.assertEqual(compare_all(4, 3), (False, True, False, False, True, True))

    def test_comparison_operators_on_strings_are_lexicographic(self):
        self.assertEqual(compare_all("apple", "banana"), (False, True, True, True, False, False))
        # Uppercase letters come before lowercase ones in Unicode.
        self.assertEqual(compare_all("Z", "a"), (False, True, True, True, False, False))

    def test_equality_between_int_and_float(self):
        self.assertEqual(compare_all(1, 1.0), (True, False, False, True, False, True))

    def test_ordering_incompatible_types_raises_type_error(self):
        with self.assertRaises(TypeError):
            compare_all(1, "1")

    def test_chained_comparison(self):
        self.assertIs(is_strictly_ascending(1, 2, 3), True)
        self.assertIs(is_strictly_ascending(1, 2, 2), False)
        self.assertIs(is_strictly_ascending(2, 2, 3), False)
        # (1 < 3) < 2 would be True < 2 -> True, but 1 < 3 < 2 means 1 < 3 and 3 < 2.
        self.assertIs(is_strictly_ascending(1, 3, 2), False)

    def test_logical_operator_precedence(self):
        # and before or; not weaker than ==.
        self.assertEqual(logical_precedence(), (True, False, True))

    def test_operator_associativity(self):
        # 2 ** (3 ** 2), (100 / 10) / 5, (10 - 4) - 3
        self.assertEqual(associativity(), (512, 2.0, 3))
        # / always gives a float, even when chained.
        self.assertIs(type(associativity()[1]), float)

    def test_or_returns_default_for_every_falsy_value(self):
        self.assertEqual(value_or_default("Ala", "anon"), "Ala")
        self.assertEqual(value_or_default(None, "anon"), "anon")
        self.assertEqual(value_or_default("", "anon"), "anon")
        self.assertEqual(value_or_default([], [0]), [0])
        # Pitfall: 0 is a valid number but still falsy.
        self.assertEqual(value_or_default(0, 10), 10)

    def test_conditional_expression(self):
        self.assertEqual(parity_label(4), "even")
        self.assertEqual(parity_label(7), "odd")
        self.assertEqual(parity_label(0), "even")
        self.assertEqual(parity_label(-3), "odd")

    def test_augmented_assignment_operators(self):
        self.assertEqual(augmented_assign(10, "+=", 3), 13)
        self.assertEqual(augmented_assign(10, "-=", 3), 7)
        self.assertEqual(augmented_assign(10, "*=", 3), 30)
        self.assertEqual(augmented_assign(10, "/=", 4), 2.5)
        self.assertEqual(augmented_assign(10, "//=", 3), 3)
        self.assertEqual(augmented_assign(10, "%=", 3), 1)
        self.assertEqual(augmented_assign(2, "**=", 10), 1024)

    def test_augmented_assignment_true_division_returns_float(self):
        self.assertIs(type(augmented_assign(10, "/=", 2)), float)

    def test_augmented_assignment_with_unknown_operator_raises_value_error(self):
        with self.assertRaises(ValueError):
            augmented_assign(10, "++", 1)

    def test_augmented_assignment_on_strings(self):
        self.assertEqual(augmented_assign("ab", "+=", "c"), "abc")
        self.assertEqual(augmented_assign("ab", "*=", 2), "abab")

    def test_plus_equals_mutates_list_in_place(self):
        items = [1, 2]
        result = extend_in_place(items, [3])
        self.assertIs(result, items)
        self.assertEqual(items, [1, 2, 3])

    def test_plus_equals_on_tuple_creates_new_object(self):
        items = (1, 2)
        result = extend_in_place(items, (3,))
        self.assertIsNot(result, items)
        self.assertEqual(result, (1, 2, 3))
        self.assertEqual(items, (1, 2))

    def test_sequence_concatenation(self):
        self.assertEqual(concatenate([1, 2], [3]), [1, 2, 3])
        self.assertEqual(concatenate((1,), (2,)), (1, 2))
        self.assertEqual(concatenate("ab", "cd"), "abcd")

    def test_concatenating_different_sequence_types_raises_type_error(self):
        with self.assertRaises(TypeError):
            concatenate([1], (2,))

    def test_sequence_repetition(self):
        self.assertEqual(repeat_sequence([0], 3), [0, 0, 0])
        self.assertEqual(repeat_sequence((1, 2), 2), (1, 2, 1, 2))
        self.assertEqual(repeat_sequence([1], 0), [])

    def test_repetition_shares_inner_objects(self):
        grid = repeat_sequence([[0]], 3)
        grid[0][0] = 9
        self.assertEqual(grid, [[9], [9], [9]])

    def test_walrus_operator_in_comprehension(self):
        self.assertEqual(squares_above([1, 2, 3, 4], 5), [9, 16])
        self.assertEqual(squares_above([-3, 1], 4), [9])
        self.assertEqual(squares_above([], 0), [])
        # Strictly greater: a square equal to the threshold is left out.
        self.assertEqual(squares_above([2, 3], 4), [9])
        # Original order is kept.
        self.assertEqual(squares_above([3, -2, 1], 0), [9, 4, 1])

    def test_arithmetic_with_floats_returns_float(self):
        self.assertEqual(floor_divide(7.5, 2), 3.0)
        self.assertIs(type(floor_divide(7.5, 2)), float)
        self.assertEqual(modulo(7.5, 2), 1.5)
        self.assertEqual(divide_with_remainder(7.5, 2), (3.0, 1.5))

    def test_int_power_has_arbitrary_precision(self):
        self.assertEqual(power(2, 100), 1267650600228229401496703205376)
        self.assertIs(type(power(2, 100)), int)

    def test_bitwise_augmented_assignment_operators(self):
        self.assertEqual(augmented_assign(6, "&=", 3), 2)
        self.assertEqual(augmented_assign(6, "|=", 3), 7)
        self.assertEqual(augmented_assign(6, "^=", 3), 5)
        self.assertEqual(augmented_assign(1, "<<=", 4), 16)
        self.assertEqual(augmented_assign(16, ">>=", 2), 4)

    def test_bool_is_an_int_in_arithmetic(self):
        # True behaves like 1 and False like 0.
        self.assertEqual(augmented_assign(True, "+=", True), 2)
        self.assertEqual(power(False, 0), 1)

    def test_bitwise_operator_precedence(self):
        # (1 | 2) == 3, 1 << (2 + 1), 1 | (2 & 0)
        self.assertEqual(bitwise_precedence(), (True, 8, 1))
        # 1 | (2 == 3) would be the int 1, not the bool True.
        self.assertIs(bitwise_precedence()[0], True)

    def test_or_short_circuits_before_modulo(self):
        # divisor is 0, so "value % divisor" is never evaluated - no ZeroDivisionError.
        self.assertIs(is_zero_or_divides(0, 7), True)
        self.assertIs(is_zero_or_divides(3, 9), True)
        self.assertIs(is_zero_or_divides(3, 10), False)

    def test_comparison_operators_on_sequences_are_lexicographic(self):
        self.assertEqual(compare_all([1, 2], [1, 3]), (False, True, True, True, False, False))
        # A shorter sequence that is a prefix of the other is smaller.
        self.assertEqual(compare_all((1, 2), (1, 2, 0)), (False, True, True, True, False, False))

    def test_set_operators(self):
        a, b = {1, 2, 3}, {2, 3, 4}
        self.assertEqual(set_operations(a, b), ({1, 2, 3, 4}, {2, 3}, {1}, {1, 4}))
        self.assertEqual(set_operations(set(), {1}), ({1}, set(), set(), {1}))

    def test_dict_merge_operator(self):
        a = {"x": 1, "y": 2}
        result = merge_dicts(a, {"y": 20, "z": 3})
        self.assertEqual(result, {"x": 1, "y": 20, "z": 3})
        self.assertEqual(a, {"x": 1, "y": 2})

    def test_unary_minus_and_plus(self):
        self.assertEqual(unary_operators(5), (-5, 5, 5))
        self.assertEqual(unary_operators(-2.5), (2.5, -2.5, -2.5))
        self.assertEqual(unary_operators(0), (0, 0, 0))

    def test_unary_plus_turns_bool_into_int(self):
        result = unary_operators(True)
        self.assertEqual(result, (-1, 1, 1))
        self.assertIs(type(result[1]), int)
        self.assertIs(type(result[2]), int)

    def test_comparison_operators_on_sets_mean_subset_and_superset(self):
        # (==, !=, <, <=, >, >=) - for sets < is "proper subset", not "smaller".
        self.assertEqual(compare_all({1}, {1, 2}), (False, True, True, True, False, False))
        self.assertEqual(compare_all({1, 2}, {1, 2}), (True, False, False, True, False, True))
        # Neither set contains the other, so every ordering comparison is False.
        self.assertEqual(compare_all({1}, {2}), (False, True, False, False, False, False))

    def test_nan_is_not_equal_to_itself(self):
        nan = float("nan")
        self.assertEqual(compare_all(nan, nan), (False, True, False, False, False, False))

    def test_matmul_operator_uses_the_class_method(self):
        # @ calls __matmul__ - here it is defined as the dot product of two vectors.
        self.assertEqual(matmul(Vector(1, 2), Vector(3, 4)), 11)

    def test_matmul_on_numbers_raises_type_error(self):
        # int does not define __matmul__.
        with self.assertRaises(TypeError):
            matmul(2, 3)

    def test_percent_on_strings_formats_text(self):
        self.assertEqual(percent_format("%s has %d items", ("cart", 3)), "cart has 3 items")
        self.assertEqual(percent_format("%.2f", 3.14159), "3.14")
        self.assertEqual(percent_format("%d%%", 50), "50%")

    def test_percent_format_with_wrong_number_of_values_raises_type_error(self):
        with self.assertRaises(TypeError):
            percent_format("%s and %s", ("only one",))
