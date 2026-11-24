import inspect
import io
import itertools
import unittest
from unittest.mock import patch

from src.functions.function_basics import (
    add_item,
    apply_twice,
    call_with,
    count_up_to,
    deep_sum,
    describe_call,
    distance,
    make_tag,
    min_max,
    modify_argument,
    print_sum,
    rectangle_area,
    sort_by_length,
    squares,
)


class TestFunctionBasics(unittest.TestCase):
    def test_function_without_return_gives_none(self):
        output = io.StringIO()
        with patch("sys.stdout", output):
            result = print_sum(2, 3)
        self.assertIsNone(result)
        self.assertEqual(output.getvalue(), "5\n")

    def test_return_multiple_values(self):
        low, high = min_max([3, 1, 2])
        self.assertEqual((low, high), (1, 3))
        self.assertEqual(min_max([7]), (7, 7))
        self.assertIsInstance(min_max([1, 2]), tuple)

    def test_min_max_of_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            min_max([])

    def test_keyword_only_parameter(self):
        self.assertEqual(make_tag("hi"), "<p>hi</p>")
        self.assertEqual(make_tag("hi", tag="b"), "<b>hi</b>")
        with self.assertRaises(TypeError):
            make_tag("hi", "b")

    def test_positional_only_parameters(self):
        self.assertEqual(distance(1, 4), 3)
        self.assertEqual(distance(4, 1), 3)
        self.assertEqual(distance(-2, 2), 4)
        with self.assertRaises(TypeError):
            distance(a=1, b=4)

    def test_mutable_default_is_not_shared_between_calls(self):
        self.assertEqual(add_item(1), [1])
        self.assertEqual(add_item(2), [2])

    def test_add_item_changes_the_given_list(self):
        items = [1]
        result = add_item(2, items)
        self.assertIs(result, items)
        self.assertEqual(items, [1, 2])

    def test_argument_is_passed_by_object_reference(self):
        items = [1]
        self.assertIsNone(modify_argument(items))
        self.assertEqual(items, [1, 99])

    def test_function_as_argument(self):
        self.assertEqual(apply_twice(lambda x: x + 3, 1), 7)
        self.assertEqual(apply_twice(str.upper, "a"), "A")
        self.assertEqual(apply_twice(abs, -5), 5)

    def test_lambda_as_sort_key(self):
        words = ["ccc", "d", "bb", "a"]
        # Equal lengths keep their order ("d" before "a"), and the original list is not changed.
        self.assertEqual(sort_by_length(words), ["d", "a", "bb", "ccc"])
        self.assertEqual(words, ["ccc", "d", "bb", "a"])
        self.assertEqual(sort_by_length([]), [])

    def test_recursion(self):
        self.assertEqual(deep_sum([1, [2, [3, 4]], 5]), 15)
        self.assertEqual(deep_sum([[[[7]]]]), 7)
        self.assertEqual(deep_sum([]), 0)
        self.assertEqual(deep_sum([[], [[]]]), 0)

    def test_argument_unpacking(self):
        self.assertEqual(call_with(pow, [2, 3], {}), 8)
        self.assertEqual(call_with(int, ["ff"], {"base": 16}), 255)
        self.assertEqual(call_with(sorted, [[3, 1, 2]], {"reverse": True}), [3, 2, 1])

    def test_all_parameter_kinds_together(self):
        self.assertEqual(describe_call(1, 2, c=3), (1, 2, (), 3, 0, {}))
        self.assertEqual(describe_call(1, b=2, c=3), (1, 2, (), 3, 0, {}))
        self.assertEqual(describe_call(1, 2, 3, 4, c=5, d=6, e=7), (1, 2, (3, 4), 5, 6, {"e": 7}))

    def test_parameter_kinds_reject_wrong_calls(self):
        self.assertEqual(describe_call(1, 2, c=3)[3], 3)
        with self.assertRaises(TypeError):
            describe_call(1, 2, 3)  # c is keyword-only, so 3 goes to args and c is missing
        with self.assertRaises(TypeError):
            describe_call(a=1, b=2, c=3)  # a is positional-only; a=1 lands in kwargs and a is missing

    def test_docstring_and_type_hints(self):
        self.assertEqual(rectangle_area(2.5, 3), 7.5)
        doc = rectangle_area.__doc__
        self.assertIsNotNone(doc)
        self.assertIn("area", doc.lower())
        self.assertEqual(rectangle_area.__annotations__, {"width": float, "height": float, "return": float})
        # Type hints are not checked when the function runs.
        self.assertEqual(rectangle_area(2, 3), 6)

    def test_generator_function(self):
        numbers = count_up_to(3)
        self.assertTrue(inspect.isgenerator(numbers))
        self.assertEqual(next(numbers), 1)
        self.assertEqual(list(numbers), [2, 3])
        with self.assertRaises(StopIteration):
            next(numbers)
        self.assertEqual(list(count_up_to(0)), [])

    def test_infinite_generator_is_lazy(self):
        values = squares()
        self.assertTrue(inspect.isgenerator(values))
        self.assertEqual(list(itertools.islice(values, 4)), [1, 4, 9, 16])
        self.assertEqual(next(values), 25)
