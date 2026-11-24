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

    def to_int_with_base(self, text, base):
        # Convert text to an integer written in the given base (2, 8, 16...).
        # With base 0 the prefix decides: "0b" binary, "0o" octal, "0x" hexadecimal.
        pass

    def int_representations(self, value):
        # Return the tuple (binary, octal, hexadecimal) strings of value, e.g. "0b1010", "0o12", "0xa".
        pass

    def complex_parts(self, value):
        # Return the tuple (real part, imaginary part, conjugate, absolute value) of a complex number.
        pass

    def make_range(self, start, stop, step):
        # Return range(start, stop, step). stop is excluded and the range is immutable.
        pass

    def make_single_tuple(self, value):
        # Return a one-element tuple. (value) is just value in parentheses - the comma makes a tuple.
        pass

    def to_bytearray(self, text):
        # Return text encoded (utf-8) as a bytearray - the mutable version of bytes.
        pass

    def is_hashable(self, value):
        # Check if value can be hashed (used as a dict key or set element).
        # Mutable containers (list, dict, set) are not hashable - hash() raises TypeError.
        pass

    def try_add_to_frozenset(self, items, item):
        # Try to add item to a frozenset. frozenset is immutable and has no add(), so this raises AttributeError.
        pass

    def is_close(self, a, b):
        # Check if two floats are equal within a small tolerance (math.isclose), instead of using ==.
        pass

    def append_inside_tuple(self, items, value):
        # items is a tuple whose first element is a list. Append value to that list and return items.
        # A tuple is immutable, but the objects inside it can still be mutable.
        pass

    def copied_lists(self):
        # Start with [1], make a copy, append 2 to the copy.
        # Return the original list - a copy is a separate object, unlike an alias.
        pass

    def dynamic_types(self):
        # Assign 5 to a variable, then "five", then None.
        # Return the tuple of type names it had after each assignment - one name can hold different types.
        pass

    def to_set(self, values):
        # Return set(values). A set keeps only unique, hashable elements and has no order.
        pass

    def to_dict(self, pairs):
        # Return dict(pairs) from (key, value) pairs. Keys are unique (the last value wins),
        # must be hashable, and the dict keeps insertion order.
        pass

    def to_tuple(self, values):
        # Return tuple(values) - the immutable counterpart of list(values).
        pass

    def to_memoryview(self, data):
        # Return memoryview(data) - a view of the same bytes buffer, without copying.
        # Writing through a view of a bytearray changes the bytearray; a view of bytes is read-only.
        pass


    def rebound_int(self):
        # Assign 5 to a, bind b to a, then do b += 1. Return a.
        # int is immutable, so += makes b point to a new object and a stays 5 (compare aliased_lists).
        pass

    def shallow_copied_nested(self):
        # Start with [[1]], make a copy, append 2 to the inner list through the copy.
        # Return the original - copy() is shallow, so the inner list is shared (compare copied_lists).
        pass
