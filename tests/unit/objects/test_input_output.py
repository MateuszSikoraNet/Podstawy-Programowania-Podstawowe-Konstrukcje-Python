import io
import os
import tempfile
import unittest
from unittest.mock import call, patch

from src.objects.input_output import Console


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = Console()

    def test_read_text(self):
        with patch("builtins.input", return_value="Ada") as input_mock:
            self.assertEqual(self.console.read_text("Name: "), "Ada")
        input_mock.assert_called_once_with("Name: ")

    def test_read_numbers(self):
        with patch("builtins.input", side_effect=["42", "2.5"]) as input_mock:
            self.assertEqual(self.console.read_integer("Age: "), 42)
            self.assertEqual(self.console.read_float("Height: "), 2.5)
        self.assertEqual(input_mock.call_args_list, [call("Age: "), call("Height: ")])
        # A whole number typed for a float is still a float.
        with patch("builtins.input", return_value="3"):
            result = self.console.read_float("Height: ")
        self.assertEqual(result, 3.0)
        self.assertIs(type(result), float)

    def test_print_greeting_and_lines(self):
        output = io.StringIO()
        with patch("sys.stdout", output):
            self.console.print_greeting("Ada")
            self.console.print_lines(["first", "second"])
            self.console.print_lines([])  # an empty list prints nothing, not even an empty line
        self.assertEqual(output.getvalue(), "Hello, Ada!\nfirst\nsecond\n")

    def test_format_output(self):
        self.assertEqual(self.console.format_output("Score", 10), "Score: 10")

    def test_input_always_returns_text(self):
        # input() never converts - "42" stays a string until you call int().
        with patch("builtins.input", return_value="42"):
            result = self.console.read_text("Number: ")
        self.assertEqual(result, "42")
        self.assertIs(type(result), str)

    def test_read_invalid_numbers_raises_value_error(self):
        with patch("builtins.input", return_value="abc"):
            with self.assertRaises(ValueError):
                self.console.read_integer("Age: ")
        # Python uses a dot, not a comma, as the decimal separator.
        with patch("builtins.input", return_value="2,5"):
            with self.assertRaises(ValueError):
                self.console.read_float("Height: ")
        # int() does not accept text with a decimal point.
        with patch("builtins.input", return_value="2.5"):
            with self.assertRaises(ValueError):
                self.console.read_integer("Age: ")

    def test_read_numbers_from_one_line(self):
        with patch("builtins.input", return_value="3 4 5") as input_mock:
            result = self.console.read_numbers("Numbers: ")
        self.assertEqual(result, [3, 4, 5])
        self.assertEqual([type(number) for number in result], [int, int, int])
        input_mock.assert_called_once_with("Numbers: ")
        with patch("builtins.input", return_value="  7   8 "):
            self.assertEqual(self.console.read_numbers("Numbers: "), [7, 8])
        with patch("builtins.input", return_value="-2 10"):
            self.assertEqual(self.console.read_numbers("Numbers: "), [-2, 10])

    def test_read_until_eof(self):
        with patch("builtins.input", side_effect=["a", "b", EOFError]) as input_mock:
            self.assertEqual(self.console.read_until_eof("> "), ["a", "b"])
        self.assertEqual(input_mock.call_args_list, [call("> ")] * 3)
        with patch("builtins.input", side_effect=EOFError):
            self.assertEqual(self.console.read_until_eof("> "), [])

    def test_read_until_eof_keeps_empty_lines_and_spaces(self):
        # Only EOFError ends the reading - an empty line is just another line.
        with patch("builtins.input", side_effect=["a", "", "  b ", "c", EOFError]):
            self.assertEqual(self.console.read_until_eof("> "), ["a", "", "  b ", "c"])

    def test_read_until_eof_does_not_hide_other_errors(self):
        with patch("builtins.input", side_effect=["a", RuntimeError("broken input")]):
            with self.assertRaises(RuntimeError):
                self.console.read_until_eof("> ")

    def test_print_values_with_default_sep_and_end(self):
        # print converts every value with str() and separates them with one space.
        output = io.StringIO()
        with patch("sys.stdout", output):
            self.console.print_values([1, 2.5, None])
        self.assertEqual(output.getvalue(), "1 2.5 None\n")

    def test_print_values_with_custom_sep_and_end(self):
        output = io.StringIO()
        with patch("sys.stdout", output):
            self.console.print_values(["a", "b"], sep=", ", end="!")
            self.console.print_values([], end="")
        self.assertEqual(output.getvalue(), "a, b!")

    def test_print_error_goes_to_stderr(self):
        output, errors = io.StringIO(), io.StringIO()
        with patch("sys.stdout", output), patch("sys.stderr", errors):
            self.console.print_error("File not found")
        self.assertEqual(errors.getvalue(), "File not found\n")
        self.assertEqual(output.getvalue(), "")

    def test_format_row_aligns_columns(self):
        self.assertEqual(self.console.format_row("Tea", 1234.5), "Tea       |  1,234.50")
        self.assertEqual(self.console.format_row("Coffee", 7), "Coffee    |      7.00")

    def test_write_and_read_file_round_trip_with_utf8(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "note.txt")
            self.console.write_file(path, "zażółć\n")
            self.assertEqual(self.console.read_file(path), "zażółć\n")
            # utf-8 stores each Polish letter in 2 bytes.
            with open(path, "rb") as file:
                self.assertEqual(file.read(), "zażółć\n".encode("utf-8"))

    def test_write_file_overwrites_content(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "note.txt")
            self.console.write_file(path, "first")
            self.console.write_file(path, "second")
            self.assertEqual(self.console.read_file(path), "second")

    def test_append_file_adds_to_the_end(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "log.txt")
            self.console.append_file(path, "a\n")
            self.console.append_file(path, "żółw\n")
            self.assertEqual(self.console.read_file(path), "a\nżółw\n")
            with open(path, "rb") as file:
                self.assertEqual(file.read(), "a\nżółw\n".encode("utf-8"))

    def test_read_lines_strips_newlines(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "lines.txt")
            self.console.write_file(path, "first\nsecond\n")
            self.assertEqual(self.console.read_lines(path), ["first", "second"])
            # Spaces and empty lines are kept, the last line may have no newline.
            self.console.write_file(path, "  zażółć \n\nlast")
            self.assertEqual(self.console.read_lines(path), ["  zażółć ", "", "last"])

    def test_read_missing_file_raises_file_not_found_error(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(FileNotFoundError):
                self.console.read_file(os.path.join(folder, "missing.txt"))

    def test_copy_binary_file(self):
        # 0xff and 0x00 are not valid utf-8 text, so this only works in binary mode.
        data = bytes([0x89, 0x50, 0x4E, 0x47, 0x00, 0xFF, 0x0A, 0x0D])
        with tempfile.TemporaryDirectory() as folder:
            source = os.path.join(folder, "image.png")
            target = os.path.join(folder, "copy.png")
            with open(source, "wb") as file:
                file.write(data)
            self.assertEqual(self.console.copy_binary(source, target), 8)
            with open(target, "rb") as file:
                self.assertEqual(file.read(), data)

    def test_copy_binary_missing_source_raises_file_not_found_error(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(FileNotFoundError):
                self.console.copy_binary(os.path.join(folder, "missing"), os.path.join(folder, "copy"))

    def test_print_to_a_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "report.txt")
            output = io.StringIO()
            with patch("sys.stdout", output):
                self.console.save_lines(path, ["zażółć", 42, None])
            # Nothing goes to the screen - print wrote to the file instead.
            self.assertEqual(output.getvalue(), "")
            with open(path, encoding="utf-8") as file:
                self.assertEqual(file.read(), "zażółć\n42\nNone\n")

    def test_read_text_keeps_spaces(self):
        with patch("builtins.input", return_value="  Ada  "):
            self.assertEqual(self.console.read_text("Name: "), "  Ada  ")

    def test_read_numbers_with_invalid_part_raises_value_error(self):
        with patch("builtins.input", return_value="1 x 3"):
            with self.assertRaises(ValueError):
                self.console.read_numbers("Numbers: ")

    def test_format_row_does_not_cut_long_values(self):
        self.assertEqual(self.console.format_row("Earl Grey Tea", 1234567.891), "Earl Grey Tea|1,234,567.89")
