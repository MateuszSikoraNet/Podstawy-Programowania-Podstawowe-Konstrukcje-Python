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

