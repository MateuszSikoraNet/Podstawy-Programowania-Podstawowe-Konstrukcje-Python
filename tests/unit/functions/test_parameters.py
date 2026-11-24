import unittest

from src.functions.parameters import build_profile, greet, power, repeat, sum_all


class TestParameters(unittest.TestCase):
    def test_default_and_keyword_parameters(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")
        self.assertEqual(greet("Ada", greeting="Hi"), "Hi, Ada!")
        self.assertEqual(power(3), 9)
        self.assertEqual(power(2, 3), 8)

    def test_variable_number_of_arguments(self):
        self.assertEqual(sum_all(1, 2, 3), 6)
        self.assertEqual(sum_all(), 0)
        self.assertEqual(build_profile("Ada", age=30), {"name": "Ada", "age": 30})

    def test_repeat(self):
        self.assertEqual(repeat("ha"), "haha")
        self.assertEqual(repeat("ha", 3, "-"), "ha-ha-ha")
        self.assertEqual(repeat("ha", 0), "")

    def test_build_profile_collects_all_keyword_arguments(self):
        self.assertEqual(build_profile("Ada"), {"name": "Ada"})
        self.assertEqual(
            build_profile("Ada", age=30, city="London"),
            {"name": "Ada", "age": 30, "city": "London"},
        )

    def test_repeat_with_separator_uses_times(self):
        self.assertEqual(repeat("ha", separator="-"), "ha-ha")
        self.assertEqual(repeat("ha", 1, "-"), "ha")
        self.assertEqual(repeat("ha", times=4, separator=" "), "ha ha ha ha")

    def test_keyword_arguments_in_any_order(self):
        self.assertEqual(greet(greeting="Hi", name="Ada"), "Hi, Ada!")
        self.assertEqual(power(exponent=3, base=2), 8)
        self.assertEqual(repeat("ab", separator=",", times=2), "ab,ab")

    def test_default_can_be_overridden_by_position(self):
        self.assertEqual(greet("Ada", "Hi"), "Hi, Ada!")
        self.assertEqual(power(5, 0), 1)

    def test_wrong_arguments_raise_type_error(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")
        with self.assertRaises(TypeError):
            greet()  # missing required argument
        with self.assertRaises(TypeError):
            greet("Ada", "Hi", "extra")  # too many positional arguments
        with self.assertRaises(TypeError):
            greet("Ada", name="Bob")  # name given twice
        with self.assertRaises(TypeError):
            greet("Ada", colour="red")  # unknown keyword argument
        with self.assertRaises(TypeError):
            build_profile("Ada", name="Bob")  # **kwargs cannot repeat a named parameter

    def test_unpacking_into_args_and_kwargs(self):
        self.assertEqual(sum_all(*[1, 2, 3]), 6)
        self.assertEqual(sum_all(2.5, 1), 3.5)
        self.assertEqual(build_profile(**{"name": "Ada", "age": 36}), {"name": "Ada", "age": 36})

    def test_build_profile_keeps_key_order(self):
        # **kwargs keeps the order of the call, and a dict keeps insertion order.
        profile = build_profile("Ada", city="London", age=36)
        self.assertEqual(list(profile), ["name", "city", "age"])
