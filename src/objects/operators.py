class OperatorCalculator:
    def modulo(self, a, b):
        # Return the remainder after dividing a by b.
        pass

    def floor_divide(self, a, b):
        # Divide a by b and round down to a whole number.
        pass

    def power(self, base, exponent):
        # Raise base to exponent.
        pass

    def divide_with_remainder(self, a, b):
        # Return the whole-number result and remainder.
        pass

    def is_even(self, value):
        # Check if value is even.
        pass

    def is_odd(self, value):
        # Check if value is odd.
        pass

    def logical_and(self, a, b):
        # Return the result of a and b.
        pass

    def logical_or(self, a, b):
        # Return the result of a or b.
        pass

    def logical_not(self, value):
        # Return the opposite of value.
        pass

    def divide(self, a, b):
        # Return a / b. True division always returns a float.
        pass

    def precedence(self):
        # Return the tuple (2 + 3 * 4, (2 + 3) * 4, -2 ** 2, 2 * 3 ** 2).
        # * binds tighter than +, and ** binds tighter than unary minus.
        pass

    def guarded_divide(self, a, b):
        # Return "a != 0 and b / a" - short-circuit must prevent the division when a is 0.
        pass

    def is_same_object(self, a, b):
        # Return whether a and b are the same object ("a is b"). Negation "is not" is not(a is b).
        pass

    def is_member(self, container, item):
        # Return whether item is a member of container ("item in container"). Negation is "not in".
        pass

    def is_not_same_object(self, a, b):
        # Return whether a and b are different objects ("a is not b").
        pass

    def is_not_member(self, container, item):
        # Return whether item is not a member of container ("item not in container").
        pass

    def bitwise_and(self, a, b):
        # Return a & b. Works bit by bit and does not short-circuit like "and".
        pass

    def bitwise_or(self, a, b):
        # Return a | b.
        pass

    def bitwise_xor(self, a, b):
        # Return a ^ b - bits that are set in exactly one of the operands.
        pass

    def bitwise_not(self, value):
        # Return ~value. For integers ~x equals -x - 1.
        pass

    def shift_left(self, value, bits):
        # Return value << bits (multiply by 2 ** bits).
        pass

    def shift_right(self, value, bits):
        # Return value >> bits (floor-divide by 2 ** bits). A negative bits count raises ValueError.
        pass

    def compare_all(self, a, b):
        # Return the tuple (a == b, a != b, a < b, a <= b, a > b, a >= b).
        pass

    def is_strictly_ascending(self, a, b, c):
        # Return the chained comparison "a < b < c" (means a < b and b < c, not (a < b) < c).
        pass

    def logical_precedence(self):
        # Return the tuple (True or False and False, not True and False, not 1 == 2).
        # "not" binds weaker than ==, "and" binds tighter than "or".
        pass

    def associativity(self):
        # Return the tuple (2 ** 3 ** 2, 100 / 10 / 5, 10 - 4 - 3).
        # ** is right-associative, the other arithmetic operators are left-associative.
        pass

    def value_or_default(self, value, default):
        # Return "value or default" - default replaces every falsy value (0, "", None, []).
        pass

    def parity_label(self, value):
        # Return "even" or "odd" using a conditional expression ("x if condition else y").
        pass

    def augmented_assign(self, value, operator, amount):
        # Apply an augmented assignment: operator is one of
        # "+=", "-=", "*=", "/=", "//=", "%=", "**=", "&=", "|=", "^=", "<<=", ">>=".
        # Raise ValueError for any other operator.
        pass

    def extend_in_place(self, container, extra):
        # Do "container += extra" and return container.
        # For a list += changes the same object; for a tuple it creates a new one.
        pass

    def concatenate(self, a, b):
        # Return a + b for sequences (lists, tuples, strings).
        pass

    def repeat_sequence(self, sequence, times):
        # Return sequence * times. Note: [[0]] * 3 repeats references to the same inner list.
        pass

    def squares_above(self, values, threshold):
        # Return the squares greater than threshold. Use the walrus operator:
        # [square for v in values if (square := v * v) > threshold]
        pass

    def bitwise_precedence(self):
        # Return the tuple (1 | 2 == 3, 1 << 2 + 1, 1 | 2 & 0).
        # Arithmetic binds tighter than shifts, & tighter than |, and | tighter than ==.
        pass

    def is_zero_or_divides(self, divisor, value):
        # Return "divisor == 0 or value % divisor == 0".
        # Short-circuit of "or" must skip the modulo when divisor is 0.
        pass

    def set_operations(self, a, b):
        # Return the tuple (a | b, a & b, a - b, a ^ b): union, intersection, difference, symmetric difference.
        pass

    def merge_dicts(self, a, b):
        # Return a | b - a new dict; on duplicate keys the value from b wins.
        pass

    def unary_operators(self, value):
        # Return the tuple (-value, +value, -(-value)) using the unary minus and plus operators.
        pass

    def matmul(self, a, b):
        # Return a @ b - the matrix multiplication operator. No built-in type supports it;
        # it works only for objects whose class defines __matmul__ (operator overloading).
        pass

    def percent_format(self, template, values):
        # Return template % values - for strings % is the printf-style formatting operator, not modulo.
        pass
