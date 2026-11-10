import io
import unittest
from unittest.mock import patch

from src.objects.input_output import Console


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = Console()

    def test_read_text(self):
        with patch("builtins.input", return_value="Ada") as input_mock:
            self.assertEqual(self.console.read_text("Name: "), "Ada")
        input_mock.assert_called_once_with("Name: ")

    def test_read_numbers(self):
        with patch("builtins.input", side_effect=["42", "2.5"]):
            self.assertEqual(self.console.read_integer("Age: "), 42)
            self.assertEqual(self.console.read_float("Height: "), 2.5)

    def test_print_greeting_and_lines(self):
        output = io.StringIO()
        with patch("sys.stdout", output):
            self.console.print_greeting("Ada")
            self.console.print_lines(["first", "second"])
        self.assertEqual(output.getvalue(), "Hello, Ada!\nfirst\nsecond\n")

    def test_format_output(self):
        self.assertEqual(self.console.format_output("Score", 10), "Score: 10")

