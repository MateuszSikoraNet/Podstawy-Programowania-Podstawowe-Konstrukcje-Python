import unittest

from src.functions.variables import accumulate, decrement, get_default_values, increment, swap


class TestVariables(unittest.TestCase):
    def test_swap(self):
        self.assertEqual(swap("left", "right"), ("right", "left"))

    def test_increment_and_decrement(self):
        self.assertEqual(increment(4), 5)
        self.assertEqual(increment(4, 3), 7)
        self.assertEqual(decrement(4), 3)
        self.assertEqual(decrement(4, 2), 2)

    def test_accumulate(self):
        self.assertEqual(accumulate([1, 2, 3]), 6)
        self.assertEqual(accumulate([]), 0)

    def test_get_default_values(self):
        self.assertEqual(get_default_values(), {"name": "", "age": 0, "active": False})

