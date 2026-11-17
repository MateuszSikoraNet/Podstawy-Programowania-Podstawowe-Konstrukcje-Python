import unittest

from src.objects.variables import Variable


class TestVariable(unittest.TestCase):
    def setUp(self):
        self.variable = Variable(10)

    def test_get_and_set(self):
        self.assertEqual(self.variable.get(), 10)
        self.variable.set(20)
        self.assertEqual(self.variable.get(), 20)

    def test_increment_and_decrement(self):
        self.variable.increment()
        self.assertEqual(self.variable.get(), 11)
        self.variable.increment(4)
        self.assertEqual(self.variable.get(), 15)
        self.variable.decrement(3)
        self.assertEqual(self.variable.get(), 12)

    def test_reset(self):
        self.variable.reset()
        self.assertEqual(self.variable.get(), 0)
        self.variable.reset(5)
        self.assertEqual(self.variable.get(), 5)

    def test_swap_with(self):
        other = Variable(3)
        self.variable.swap_with(other)
        self.assertEqual(self.variable.get(), 3)
        self.assertEqual(other.get(), 10)

