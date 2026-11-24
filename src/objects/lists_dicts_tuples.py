class Inventory:
    def __init__(self):
        # Create an empty dictionary for the items.
        pass

    def add_item(self, name, quantity=1):
        # Add quantity to the item count.
        pass

    def remove_item(self, name, quantity=1):
        # Subtract quantity from the item count.
        # Raise ValueError (and change nothing) if quantity is more than the current count -
        # a missing item has count 0. When the count reaches 0, remove the item completely.
        pass

    def get_quantity(self, name):
        # Return zero if the item is missing.
        pass

    def get_items(self):
        # Return all items and their counts as a NEW dict (a copy) - changing it must not change the inventory.
        pass
