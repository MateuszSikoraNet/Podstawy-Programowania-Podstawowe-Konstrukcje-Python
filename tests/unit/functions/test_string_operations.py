import unittest

from src.functions.string_operations import (
    capitalize_words,
    count_character,
    count_vowels,
    count_words,
    is_palindrome,
    reverse_string,
    truncate,
)


class TestStringOperations(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")

    def test_is_palindrome_ignores_case_and_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Education"), 5)
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_capitalize_and_count(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(count_words("  hello   world  "), 2)
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_character("banana", "a"), 3)

    def test_truncate(self):
        self.assertEqual(truncate("Hello world", 8), "Hello...")
        self.assertEqual(truncate("Hello", 8), "Hello")
        self.assertEqual(truncate("Hello world", 8, suffix="!"), "Hello w!")

