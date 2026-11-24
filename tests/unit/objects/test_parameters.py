import unittest

from src.objects.parameters import Greeter


class TestGreeter(unittest.TestCase):
    def test_greet_with_custom_format(self):
        greeter = Greeter("Welcome", ".")
        self.assertEqual(greeter.greet("Ada"), "Welcome, Ada.")

    def test_greet_with_default_format(self):
        self.assertEqual(Greeter().greet("Ada"), "Hello, Ada!")

    def test_greeter_keyword_arguments_skip_earlier_defaults(self):
        self.assertEqual(Greeter(punctuation="?").greet("Ada"), "Hello, Ada?")
        self.assertEqual(Greeter(greeting="Hi").greet("Ada"), "Hi, Ada!")
        self.assertEqual(Greeter("Hi").greet(name="Ada"), "Hi, Ada!")

    def test_greeter_wrong_arguments_raise_type_error(self):
        greeter = Greeter()
        self.assertEqual(greeter.greet("Ada"), "Hello, Ada!")
        with self.assertRaises(TypeError):
            greeter.greet()  # self is passed automatically, name is missing
        with self.assertRaises(TypeError):
            Greeter("Hi", "!", "extra")
        with self.assertRaises(TypeError):
            Greeter(colour="red")
