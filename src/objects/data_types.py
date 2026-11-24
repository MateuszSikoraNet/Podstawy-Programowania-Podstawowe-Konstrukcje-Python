class TypeConverter:
    def get_type_name(self, value):
        # Return the type name of value.
        pass

    def to_int(self, value):
        # Convert value to an integer.
        pass

    def to_float(self, value):
        # Convert value to a float.
        pass

    def to_str(self, value):
        # Convert value to a string.
        pass

    def to_bool(self, value):
        # Convert value to a boolean.
        pass

    def is_integer(self, value):
        # Check if value is an integer. bool is not an integer here.
        pass

    def is_float(self, value):
        # Check if value is a float.
        pass

    def true_division_type(self, a, b):
        # Return the type name of a / b. True division always returns a float.
        pass

    def floor_division_type(self, a, b):
        # Return the type name of a // b. The result type depends on the operands.
        pass

    def truncate(self, value):
        # Return value as an integer truncated toward zero (not rounded).
        pass

    def sum_of_tenths(self):
        # Return the sum of 0.1 and 0.2.
        pass

    def repeat(self, text, times):
        # Return text repeated times times (text * times).
        pass

    def to_bytes(self, text):
        # Return text encoded to bytes (utf-8).
        pass

    def is_none(self, value):
        # Check if value is None. Only None - not 0, "", [] or False.
        pass

    def add_one(self, value):
        # Return value + 1. Must stay exact even for very large integers.
        pass

    def append_item(self, items, item):
        # Append item to the list in place and return None.
        pass

    def try_assign_string_index(self, text):
        # Try to assign "J" to text[0]. Strings are immutable, so this raises TypeError.
        pass

    def try_assign_tuple_index(self, items):
        # Try to assign 0 to items[0]. Tuples are immutable, so this raises TypeError.
        pass

    def to_char(self, code):
        # Return the one-character string for this Unicode code point.
        pass

    def to_code(self, char):
        # Return the Unicode code point of this one-character string.
        pass

    def to_list(self, text):
        # Return the string as a list of single characters.
        pass

    def join_chars(self, chars):
        # Join the list of characters into one string (no separator).
        pass

    def round_value(self, value):
        # Return value rounded to the nearest integer using round().
        pass

    def mixed_sum_type(self, a, b):
        # Return the type name of a + b.
        pass

    def is_nan(self, value):
        # Check if value is NaN. NaN is the only value not equal to itself.
        pass

    def concat_str_int(self, text, number):
        # Return text + number. Python does not convert implicitly, so this raises TypeError.
        pass

    def from_bytes(self, data):
        # Decode bytes to a string (utf-8).
        pass

    def aliased_lists(self):
        # Start with [1], bind a second name to the same list, append 2 via the second name.
        # Return the list seen through the first name - both names refer to one object.
        pass
