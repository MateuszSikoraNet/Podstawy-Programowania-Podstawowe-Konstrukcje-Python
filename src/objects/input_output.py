class Console:
    def read_text(self, prompt):
        # Read text from input.
        # Return it exactly as typed - spaces at the start and end are kept.
        pass

    def read_integer(self, prompt):
        # Read an integer from input.
        pass

    def read_float(self, prompt):
        # Read a float from input.
        pass

    def print_greeting(self, name):
        # Print a greeting for name.
        pass

    def print_lines(self, lines):
        # Print each line on a new line.
        # An empty list prints nothing (not even an empty line).
        pass

    def format_output(self, label, value):
        # Return label and value separated by a colon.
        pass

    def read_numbers(self, prompt):
        # Read one line with integers separated by whitespace and return them as a list of ints.
        # A part that is not an integer raises ValueError (do not skip it).
        pass

    def read_until_eof(self, prompt):
        # Keep reading lines until input() raises EOFError (end of input, Ctrl+D) and return them as a list.
        pass

    def print_values(self, values, sep=" ", end="\n"):
        # Print all values in one call, separated by sep and finished with end (print's sep and end).
        pass

    def print_error(self, message):
        # Print message to standard error (sys.stderr), not to standard output.
        pass

    def format_row(self, name, price):
        # Return name left-aligned in 10 characters, "|", then price right-aligned in 10 characters
        # with a thousands separator and 2 decimal places, e.g. "Tea       |  1,234.50".
        # A width is a minimum: longer names and prices are not cut.
        pass

    def write_file(self, path, text):
        # Write text to the file (utf-8). Mode "w" creates the file or overwrites its content.
        pass

    def append_file(self, path, text):
        # Append text to the end of the file (utf-8). Mode "a" creates the file if it is missing.
        pass

    def read_file(self, path):
        # Return the whole content of the file (utf-8). A missing file raises FileNotFoundError.
        pass

    def read_lines(self, path):
        # Return the lines of the file (utf-8) as a list, without the trailing newline characters.
        pass

    def copy_binary(self, source, target):
        # Copy the file source to target byte by byte and return the number of bytes copied.
        # Open both files in binary mode ("rb" / "wb"): data is bytes, nothing is decoded,
        # so it works for images and other non-text files. A missing source raises FileNotFoundError.
        pass

    def save_lines(self, path, lines):
        # Write each line to the file (utf-8) with print(line, file=file) - print adds the newline.
        # Values that are not strings are converted like print() does on screen.
        pass
