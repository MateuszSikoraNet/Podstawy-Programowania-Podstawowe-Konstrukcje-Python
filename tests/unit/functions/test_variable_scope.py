import unittest

from src.functions.variable_scope import (
    get_counter,
    get_global_value,
    increment_counter,
    make_counter,
    make_multiplier,
    reset_counter,
    set_local_value,
)


class TestVariableScope(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def test_global_counter(self):
        self.assertEqual(get_counter(), 0)
        self.assertEqual(increment_counter(), 1)
        self.assertEqual(increment_counter(), 2)
        self.assertEqual(get_counter(), 2)
        reset_counter()
        self.assertEqual(get_counter(), 0)

    def test_local_variable_does_not_change_global_value(self):
        self.assertEqual(get_global_value(), 10)
        set_local_value(25)
        self.assertEqual(get_global_value(), 10)

    def test_counter_closure(self):
        counter = make_counter(3)
        self.assertTrue(callable(counter))
        self.assertEqual(counter(), 4)
        self.assertEqual(counter(), 5)

    def test_multiplier_closure(self):
        triple = make_multiplier(3)
        self.assertTrue(callable(triple))
        self.assertEqual(triple(4), 12)
