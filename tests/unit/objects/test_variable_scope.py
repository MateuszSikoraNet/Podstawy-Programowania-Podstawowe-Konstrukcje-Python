import unittest

from src.objects.variable_scope import Counter


class TestCounter(unittest.TestCase):
    def setUp(self):
        Counter.reset_total_instances()

    def test_instance_and_class_attributes(self):
        first = Counter(2)
        second = Counter(10)
        self.assertEqual(first.get(), 2)
        self.assertEqual(second.get(), 10)
        self.assertEqual(Counter.total_instances, 2)
        first.increment()
        self.assertEqual(first.get(), 3)
        self.assertEqual(second.get(), 10)

    def test_increment_temporarily_does_not_change_state(self):
        counter = Counter(5)
        self.assertEqual(counter.increment_temporarily(3), 8)
        self.assertEqual(counter.get(), 5)

