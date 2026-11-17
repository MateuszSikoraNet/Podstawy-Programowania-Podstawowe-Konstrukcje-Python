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

