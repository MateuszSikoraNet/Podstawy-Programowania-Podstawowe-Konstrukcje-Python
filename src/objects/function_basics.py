class FunctionTools:
    def print_sum(self, a, b):
        # Print a + b and return nothing.
        # A function without return gives None - printing a value is not the same as returning it.
        pass

    def min_max(self, values):
        # Return two values: the smallest and the largest (return low, high - this is one tuple).
        # An empty list raises ValueError (as min() does).
        pass

    def make_tag(self, text, *, tag="p"):
        # Return text wrapped in an HTML tag, e.g. "<p>hi</p>".
        # tag is keyword-only (after *): make_tag("hi", "b") raises TypeError, make_tag("hi", tag="b") works.
        pass

    def distance(self, a, b, /):
        # Return the distance between two numbers (always non-negative).
        # a and b are positional-only (before /): distance(a=1, b=2) raises TypeError.
        pass

    def add_item(self, item, items=None):
        # Append item to items and return items. Without items start a new list for every call.
        # Do not use items=[] as the default - that one list is created once and shared by all calls.
        pass

    def modify_argument(self, items):
        # Append 99 to items, then assign a new empty list to items. Return nothing.
        # The caller sees the append (same object), but not the assignment (it only rebinds the local name).
        pass

    def apply_twice(self, function, value):
        # Return function(function(value)). Functions are values: they can be passed as arguments.
        pass

    def sort_by_length(self, words):
        # Return the words sorted from shortest to longest. Use sorted() with key=lambda word: len(word).
        # Words of equal length keep their original order.
        pass

    def deep_sum(self, items):
        # Return the sum of all numbers in a list that can contain nested lists, e.g. [1, [2, [3]]] -> 6.
        # Use recursion: call self.deep_sum for every element that is a list. The base case is a plain number.
        pass

    def call_with(self, function, args, kwargs):
        # Return function called with args unpacked as positional and kwargs as keyword arguments:
        # function(*args, **kwargs).
        pass

    def describe_call(self, a, /, b, *args, c, d=0, **kwargs):
        # Return the tuple (a, b, args, c, d, kwargs) to show how arguments are matched to parameters:
        # a is positional-only, b is positional or keyword, args collects extra positional arguments (a tuple),
        # c is keyword-only and required, d is keyword-only with a default, kwargs collects other keyword arguments (a dict).
        pass

    def rectangle_area(self, width: float, height: float) -> float:
        # Return width * height.
        # Also write a docstring - a string literal as the first line of the body, e.g.
        # """Return the area of a rectangle.""" - it becomes rectangle_area.__doc__ and is shown by help().
        # The ": float" and "-> float" annotations are type hints: documentation only, Python does not enforce them.
        pass

    def count_up_to(self, limit):
        # A generator function: use yield to produce 1, 2, ..., limit one at a time (no list).
        # Calling it does not run the body yet - it returns a generator; next() runs it until the next yield,
        # and when the body ends next() raises StopIteration.
        pass

    def squares(self):
        # An infinite generator: yield 1, 4, 9, 16, ... forever (while True + yield).
        # It works because values are produced lazily, only when asked for.
        pass
