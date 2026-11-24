import unittest

from src.functions.error_handling import (
    check_positive,
    classify_lookup,
    convert_status,
    convert_with_log,
    describe_error,
    divide_report,
    get_element,
    load_setting,
    lookup,
    parse_int,
    parse_or_log,
    safe_divide,
    safe_get,
    validate_age,
)


class TestErrorHandling(unittest.TestCase):
    def test_safe_divide(self):
        self.assertEqual(safe_divide(10, 2), 5)
        self.assertIsNone(safe_divide(10, 0))
        self.assertEqual(safe_divide(10, 0, default=-1), -1)

    def test_parse_int(self):
        self.assertEqual(parse_int("42"), 42)
        self.assertIsNone(parse_int("invalid"))
        self.assertEqual(parse_int("invalid", default=0), 0)

    def test_get_element(self):
        self.assertEqual(get_element(["a", "b"], 1), "b")
        with self.assertRaises(IndexError):
            get_element(["a"], 2)

    def test_safe_get(self):
        self.assertEqual(safe_get({"name": "Ada"}, "name"), "Ada")
        self.assertEqual(safe_get({}, "name", default="unknown"), "unknown")

    def test_validate_age(self):
        self.assertTrue(validate_age(0))
        self.assertTrue(validate_age(120))
        with self.assertRaises(ValueError):
            validate_age(-1)
        with self.assertRaises(ValueError):
            validate_age(121)

    def test_safe_divide_is_true_division(self):
        self.assertEqual(safe_divide(7, 2), 3.5)
        self.assertEqual(safe_divide(0, 5), 0)

    def test_parse_int_edge_cases(self):
        self.assertEqual(parse_int("-5"), -5)
        self.assertEqual(parse_int(" 7 "), 7)
        self.assertEqual(parse_int("3.5", default=0), 0)
        # int(None) raises TypeError, not ValueError - catch both (except (ValueError, TypeError)).
        self.assertEqual(parse_int(None, default=0), 0)

    def test_get_element_with_negative_index(self):
        self.assertEqual(get_element(["a", "b"], -1), "b")
        with self.assertRaises(IndexError):
            get_element(["a", "b"], -3)

    def test_safe_get_returns_existing_falsy_value(self):
        self.assertEqual(safe_get({"count": 0}, "count", default=5), 0)
        self.assertIsNone(safe_get({}, "name"))

    def test_validate_age_returns_true(self):
        self.assertIs(validate_age(50), True)

    def test_try_except_else_finally(self):
        self.assertEqual(divide_report(1, 2), ["try", "else", "finally"])
        self.assertEqual(divide_report(1, 0), ["try", "except", "finally"])

    def test_finally_runs_even_when_returning_or_raising(self):
        log = []
        self.assertEqual(convert_with_log("5", log), 5)
        self.assertEqual(log, ["closed"])
        with self.assertRaises(ValueError):
            convert_with_log("x", log)
        self.assertEqual(log, ["closed", "closed"])

    def test_exception_object_carries_a_message(self):
        self.assertEqual(describe_error("12"), "OK")
        self.assertEqual(describe_error("abc"), "Error: invalid literal for int() with base 10: 'abc'")

    def test_raise_with_message_and_cause(self):
        self.assertEqual(load_setting({"mode": "dark"}, "mode"), "dark")
        with self.assertRaises(ValueError) as context:
            load_setting({}, "mode")
        self.assertEqual(str(context.exception), "Missing setting: mode")
        self.assertIsInstance(context.exception.__cause__, KeyError)

    def test_bare_raise_re_raises_the_same_error(self):
        log = []
        self.assertEqual(parse_or_log("3", log), 3)
        self.assertEqual(log, [])
        with self.assertRaises(ValueError) as context:
            parse_or_log("x", log)
        self.assertEqual(log, ["x"])
        self.assertIn("invalid literal", str(context.exception))

    def test_assert_raises_assertion_error(self):
        self.assertEqual(check_positive(3), 3)
        self.assertEqual(check_positive(1), 1)
        with self.assertRaises(AssertionError) as context:
            check_positive(0)
        self.assertEqual(str(context.exception), "value must be positive")

    def test_catch_a_parent_exception_class(self):
        self.assertEqual(lookup([10, 20], 1), 20)
        self.assertEqual(lookup([10, 20], 5, "none"), "none")
        self.assertEqual(lookup({"a": 1}, "b", 0), 0)
        self.assertTrue(issubclass(IndexError, LookupError))
        self.assertTrue(issubclass(KeyError, LookupError))
        with self.assertRaises(TypeError):
            lookup([10, 20], "a")

    def test_separate_except_blocks(self):
        self.assertEqual(convert_status("12"), "ok")
        self.assertEqual(convert_status("abc"), "bad value")
        self.assertEqual(convert_status(None), "bad type")
        self.assertEqual(convert_status([1]), "bad type")

    def test_specific_except_block_must_come_first(self):
        self.assertEqual(classify_lookup({"a": 1}, "a"), 1)
        self.assertEqual(classify_lookup({"a": 1}, "b"), "missing key")
        # IndexError is a LookupError but not a KeyError, so it reaches the second block.
        self.assertEqual(classify_lookup([1], 5), "lookup failed")
