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

    def test_default_arguments(self):
        counter = Counter()
        self.assertEqual(counter.get(), 0)
        self.assertEqual(counter.increment_temporarily(), 1)
        self.assertEqual(counter.get(), 0)

    def test_increment_by_amount(self):
        counter = Counter(1)
        counter.increment(5)
        self.assertEqual(counter.get(), 6)

    def test_class_attribute_is_read_through_every_instance(self):
        first = Counter()
        second = Counter()
        self.assertEqual(first.total_instances, 2)
        self.assertEqual(second.total_instances, 2)

    def test_assigning_through_instance_shadows_class_attribute(self):
        first = Counter()
        second = Counter()
        first.total_instances = 100  # creates an instance attribute, the class one is unchanged
        self.assertEqual(first.total_instances, 100)
        self.assertEqual(second.total_instances, 2)
        self.assertEqual(Counter.total_instances, 2)

    def test_each_instance_has_its_own_attributes(self):
        first = Counter(1)
        second = Counter(1)
        first.increment(4)
        self.assertEqual(first.get(), 5)
        self.assertEqual(second.get(), 1)
