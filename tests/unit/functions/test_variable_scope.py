import unittest

from src.functions.variable_scope import (
    comprehension_variable,
    count_locally,
    get_counter,
    get_global_value,
    increment_counter,
    last_loop_value,
    make_adders,
    make_adders_late_binding,
    make_counter,
    make_counter_without_nonlocal,
    make_multiplier,
    reset_counter,
    set_local_value,
    shadowed_builtin,
    try_increment_without_global,
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

    def test_counter_closure_default_start(self):
        self.assertEqual(make_counter()(), 1)

    def test_each_closure_has_its_own_state(self):
        first = make_counter(0)
        second = make_counter(10)
        self.assertEqual(first(), 1)
        self.assertEqual(second(), 11)
        self.assertEqual(first(), 2)
        double = make_multiplier(2)
        triple = make_multiplier(3)
        self.assertEqual(double(5), 10)
        self.assertEqual(triple(5), 15)

    def test_assignment_without_global_makes_the_name_local(self):
        increment_counter()
        with self.assertRaises(UnboundLocalError):
            try_increment_without_global()
        self.assertEqual(get_counter(), 1)

    def test_no_block_scope(self):
        self.assertEqual(last_loop_value([1, 2, 3]), 3)
        self.assertEqual(last_loop_value(["only"]), "only")
        self.assertIsNone(last_loop_value([]))

    def test_comprehension_has_its_own_scope(self):
        self.assertEqual(comprehension_variable(), "outer")

    def test_local_name_shadows_builtin(self):
        with self.assertRaises(TypeError):
            shadowed_builtin([1, 2])
        # Only the local scope was affected - the built-in max() still works here.
        self.assertEqual(max([1, 2]), 2)

    def test_assignment_without_nonlocal_makes_the_name_local(self):
        counter = make_counter_without_nonlocal()
        self.assertTrue(callable(counter))
        with self.assertRaises(UnboundLocalError):
            counter()

    def test_local_variables_live_only_during_one_call(self):
        self.assertEqual(count_locally(), 1)
        self.assertEqual(count_locally(), 1)
        self.assertIs(type(count_locally()), int)
        # A closure keeps its state between calls instead.
        counter = make_counter()
        counter()
        self.assertEqual(counter(), 2)

    def test_closures_in_a_loop_bind_late(self):
        adders = make_adders_late_binding(3)
        self.assertEqual(len(adders), 3)
        self.assertEqual([add(10) for add in adders], [12, 12, 12])

    def test_default_argument_freezes_the_loop_value(self):
        adders = make_adders(3)
        self.assertEqual([add(10) for add in adders], [10, 11, 12])
        self.assertEqual(make_adders(0), [])

    def test_loop_variable_after_looping_over_any_iterable(self):
        # A dict loops over its keys; an iterator cannot be indexed - only a for loop works for both.
        self.assertEqual(last_loop_value({"a": 1, "b": 2}), "b")
        self.assertEqual(last_loop_value(iter([4, 5])), 5)
        self.assertEqual(last_loop_value("abc"), "c")

    def test_late_binding_uses_the_last_loop_value(self):
        self.assertEqual([add(0) for add in make_adders_late_binding(4)], [3, 3, 3, 3])
        self.assertEqual([add(5) for add in make_adders_late_binding(1)], [5])
