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

    def test_is_palindrome_returns_bool(self):
        self.assertIs(self.analyzer.is_palindrome("Kajak"), True)
        self.assertIs(self.analyzer.is_palindrome("ab"), False)
        self.assertIs(self.analyzer.is_palindrome(""), True)

    def test_count_vowels_counts_every_occurrence(self):
        self.assertEqual(self.analyzer.count_vowels("banana"), 3)
        self.assertEqual(self.analyzer.count_vowels("AEIOU"), 5)

    def test_count_character_is_case_sensitive(self):
        self.assertEqual(self.analyzer.count_character("Banana", "b"), 0)
        self.assertEqual(self.analyzer.count_character("Banana", "B"), 1)

    def test_truncate_text_of_exactly_max_length(self):
        self.assertEqual(self.analyzer.truncate("Hello", 5), "Hello")
        self.assertEqual(self.analyzer.truncate("Hello!", 5), "He...")

    def test_case_methods(self):
        self.assertEqual(self.analyzer.case_variants("hello WORLD"), ("HELLO WORLD", "hello world", "Hello world"))

    def test_strings_are_immutable_methods_return_new_strings(self):
        text = "  Hello World  "
        self.assertEqual(self.analyzer.normalize(text), "hello world")
        self.assertEqual(text, "  Hello World  ")
        self.assertEqual(self.analyzer.normalize("\tTab\n"), "tab")

    def test_replace_every_occurrence(self):
        self.assertEqual(self.analyzer.replace_word("cat and cat", "cat", "dog"), "dog and dog")
        self.assertEqual(self.analyzer.replace_word("abc", "x", "y"), "abc")

    def test_find_position(self):
        self.assertEqual(self.analyzer.find_position("hello", "l"), 2)
        self.assertEqual(self.analyzer.find_position("hello", "lo"), 3)
        self.assertEqual(self.analyzer.find_position("hello", "z"), -1)

    def test_split_with_separator(self):
        self.assertEqual(self.analyzer.split_csv(" a, b ,c"), ["a", "b", "c"])
        self.assertEqual(self.analyzer.split_csv("a,,b"), ["a", "", "b"])
        self.assertEqual(self.analyzer.split_csv("one"), ["one"])

    def test_join_with_separator(self):
        self.assertEqual(self.analyzer.join_words(["a", "b", "c"], ", "), "a, b, c")
        self.assertEqual(self.analyzer.join_words([], "-"), "")
        with self.assertRaises(TypeError):
            self.analyzer.join_words(["a", 1], "-")

    def test_startswith_and_endswith(self):
        self.assertEqual(self.analyzer.starts_and_ends("report.pdf", "rep", ".pdf"), (True, True))
        self.assertEqual(self.analyzer.starts_and_ends("report.pdf", "Rep", ".txt"), (False, False))

    def test_string_indexing(self):
        self.assertEqual(self.analyzer.char_at("Python", 0), "P")
        self.assertEqual(self.analyzer.char_at("Python", -1), "n")
        with self.assertRaises(IndexError):
            self.analyzer.char_at("Python", 6)

    def test_escape_sequences_and_raw_strings(self):
        self.assertEqual(self.analyzer.escape_lengths(), (3, 3, 4, 1))

    def test_character_classes(self):
        self.assertEqual(self.analyzer.classify_char("7"), "digit")
        self.assertEqual(self.analyzer.classify_char("ż"), "letter")
        self.assertEqual(self.analyzer.classify_char(" "), "space")
        self.assertEqual(self.analyzer.classify_char("\n"), "space")
        self.assertEqual(self.analyzer.classify_char("?"), "other")

    def test_capitalize_words_changes_only_first_letters(self):
        self.assertEqual(self.analyzer.capitalize_words("hELLO wORLD"), "HELLO WORLD")
        self.assertEqual(self.analyzer.capitalize_words("hello  world"), "Hello  World")
        self.assertEqual(self.analyzer.capitalize_words("it's ok"), "It's Ok")
        self.assertEqual(self.analyzer.capitalize_words(""), "")

    def test_is_palindrome_does_not_ignore_punctuation(self):
        self.assertIs(self.analyzer.is_palindrome("Kobyła ma mały bok"), True)
        self.assertIs(self.analyzer.is_palindrome("Was it a car, or a cat I saw?"), False)
        self.assertIs(self.analyzer.is_palindrome("a\tb a"), False)

    def test_count_vowels_only_aeiou(self):
        self.assertEqual(self.analyzer.count_vowels("Yes"), 1)
        self.assertEqual(self.analyzer.count_vowels("Mały ŻÓŁW"), 1)

    def test_count_words_with_any_whitespace(self):
        self.assertEqual(self.analyzer.count_words("a\tb\nc"), 3)
        self.assertEqual(self.analyzer.count_words("one, two"), 2)

    def test_truncate_never_longer_than_max_length(self):
        self.assertEqual(self.analyzer.truncate("Hello world", 3), "...")
        self.assertEqual(self.analyzer.truncate("Hello world", 2), "He")
        self.assertEqual(self.analyzer.truncate("Hello world", 0), "")
        self.assertEqual(self.analyzer.truncate("Hi", 2), "Hi")

    def test_normalize_uses_lower(self):
        self.assertEqual(self.analyzer.normalize(" Straße "), "straße")

    def test_split_csv_strips_any_whitespace(self):
        self.assertEqual(self.analyzer.split_csv("a,\tb\n"), ["a", "b"])
