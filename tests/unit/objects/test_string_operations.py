import unittest

from src.objects.string_operations import TextAnalyzer


class TestTextAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = TextAnalyzer()

    def test_reverse_string(self):
        self.assertEqual(self.analyzer.reverse_string("hello"), "olleh")
        self.assertEqual(self.analyzer.reverse_string(""), "")

    def test_is_palindrome_ignores_case_and_spaces(self):
        self.assertTrue(self.analyzer.is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(self.analyzer.is_palindrome("hello"))

    def test_count_vowels(self):
        self.assertEqual(self.analyzer.count_vowels("Education"), 5)
        self.assertEqual(self.analyzer.count_vowels("rhythm"), 0)

    def test_capitalize_and_count(self):
        self.assertEqual(self.analyzer.capitalize_words("hello world"), "Hello World")
        self.assertEqual(self.analyzer.count_words("  hello   world  "), 2)
        self.assertEqual(self.analyzer.count_words(""), 0)
        self.assertEqual(self.analyzer.count_character("banana", "a"), 3)

    def test_truncate(self):
        self.assertEqual(self.analyzer.truncate("Hello world", 8), "Hello...")
        self.assertEqual(self.analyzer.truncate("Hello", 8), "Hello")
        self.assertEqual(self.analyzer.truncate("Hello world", 8, suffix="!"), "Hello w!")

