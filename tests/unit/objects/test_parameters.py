import unittest

from src.objects.parameters import Greeter


class TestGreeter(unittest.TestCase):
    def test_greet_with_custom_format(self):
        greeter = Greeter("Welcome", ".")
        self.assertEqual(greeter.greet("Ada"), "Welcome, Ada.")

    def test_greet_with_default_format(self):
        self.assertEqual(Greeter().greet("Ada"), "Hello, Ada!")

