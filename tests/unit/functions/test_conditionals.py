import unittest

from src.functions.conditionals import absolute_value, classify_temperature, fizz_buzz, grade, max_of_two, sign


class TestConditionals(unittest.TestCase):
    def test_sign_and_absolute_value(self):
        self.assertEqual(sign(-4), -1)
        self.assertEqual(sign(0), 0)
        self.assertEqual(sign(4), 1)
        self.assertEqual(absolute_value(-4), 4)

    def test_max_of_two(self):
        self.assertEqual(max_of_two(3, 8), 8)
        self.assertEqual(max_of_two(5, 5), 5)

    def test_grade_boundaries(self):
        self.assertEqual(grade(90), "A")
        self.assertEqual(grade(80), "B")
        self.assertEqual(grade(70), "C")
        self.assertEqual(grade(60), "D")
        self.assertEqual(grade(59), "F")

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(7), 7)

    def test_classify_temperature(self):
        self.assertEqual(classify_temperature(10), "cold")
        self.assertEqual(classify_temperature(20), "warm")
        self.assertEqual(classify_temperature(30), "hot")

