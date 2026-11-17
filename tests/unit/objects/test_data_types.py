import unittest

from src.objects.data_types import TypeConverter


class TestTypeConverter(unittest.TestCase):
    def setUp(self):
        self.converter = TypeConverter()

    def test_get_type_name(self):
        self.assertEqual(self.converter.get_type_name(5), "int")
        self.assertEqual(self.converter.get_type_name("hello"), "str")

    def test_convert_values(self):
        self.assertEqual(self.converter.to_int("42"), 42)
        self.assertEqual(self.converter.to_float("3.5"), 3.5)
        self.assertEqual(self.converter.to_str(12), "12")

    def test_convert_to_bool(self):
        self.assertFalse(self.converter.to_bool(0))
        self.assertTrue(self.converter.to_bool("hello"))

    def test_is_integer(self):
        self.assertTrue(self.converter.is_integer(7))
        self.assertFalse(self.converter.is_integer(7.5))

    def test_invalid_numeric_conversion_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.converter.to_int("not a number")

