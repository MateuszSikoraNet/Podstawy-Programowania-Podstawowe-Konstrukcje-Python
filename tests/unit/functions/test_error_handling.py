import unittest

from src.functions.error_handling import get_element, parse_int, safe_divide, safe_get, validate_age


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

