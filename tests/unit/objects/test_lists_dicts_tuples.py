import unittest

from src.objects.lists_dicts_tuples import Inventory


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()

    def test_add_and_get_items(self):
        self.inventory.add_item("apples", 3)
        self.inventory.add_item("oranges", 2)
        self.assertEqual(self.inventory.get_quantity("apples"), 3)
        self.assertEqual(self.inventory.get_items(), {"apples": 3, "oranges": 2})

    def test_add_existing_item_and_remove(self):
        self.inventory.add_item("apples", 2)
        self.inventory.add_item("apples", 3)
        self.assertEqual(self.inventory.get_quantity("apples"), 5)
        self.inventory.remove_item("apples", 2)
        self.assertEqual(self.inventory.get_quantity("apples"), 3)

    def test_unknown_item_has_zero_quantity(self):
        self.assertEqual(self.inventory.get_quantity("missing"), 0)

    def test_default_quantity_is_one(self):
        self.inventory.add_item("pears")
        self.inventory.add_item("pears")
        self.assertEqual(self.inventory.get_quantity("pears"), 2)
        self.inventory.remove_item("pears")
        self.assertEqual(self.inventory.get_quantity("pears"), 1)

    def test_removing_more_than_available_raises_value_error(self):
        self.inventory.add_item("apples", 2)
        with self.assertRaises(ValueError):
            self.inventory.remove_item("apples", 3)
        self.assertEqual(self.inventory.get_quantity("apples"), 2)

    def test_removing_missing_item_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.inventory.remove_item("missing")
        self.assertEqual(self.inventory.get_items(), {})

    def test_item_with_zero_count_is_removed(self):
        self.inventory.add_item("apples", 2)
        self.inventory.add_item("pears", 1)
        self.inventory.remove_item("apples", 2)
        self.assertEqual(self.inventory.get_items(), {"pears": 1})
        self.assertEqual(self.inventory.get_quantity("apples"), 0)

    def test_get_items_returns_a_copy(self):
        self.inventory.add_item("apples", 2)
        items = self.inventory.get_items()
        items["apples"] = 100
        items["stolen"] = 1
        self.assertEqual(self.inventory.get_items(), {"apples": 2})
