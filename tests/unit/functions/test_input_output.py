import io
import unittest
from unittest.mock import patch

from src.functions.input_output import format_output, print_greeting, print_lines, read_float, read_integer, read_text


class TestInputOutput(unittest.TestCase):
    def test_read_text(self):
        with patch("builtins.input", return_value="Ada") as input_mock:
            self.assertEqual(read_text("Name: "), "Ada")
        input_mock.assert_called_once_with("Name: ")

    def test_read_numbers(self):
        with patch("builtins.input", side_effect=["42", "2.5"]):
            self.assertEqual(read_integer("Age: "), 42)
            self.assertEqual(read_float("Height: "), 2.5)

    def test_print_greeting_and_lines(self):
        output = io.StringIO()
        with patch("sys.stdout", output):
            print_greeting("Ada")
            print_lines(["first", "second"])
        self.assertEqual(output.getvalue(), "Hello, Ada!\nfirst\nsecond\n")

    def test_format_output(self):
        self.assertEqual(format_output("Score", 10), "Score: 10")

