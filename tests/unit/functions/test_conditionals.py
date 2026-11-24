import unittest

from src.functions.conditionals import (
    absolute_value,
    clamp_to_limit,
    classify_temperature,
    fizz_buzz,
    grade,
    http_status,
    is_leap_year,
    max_of_two,
    sign,
    ticket_price,
)


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

    def test_absolute_value_of_non_negative_is_unchanged(self):
        # A value that is not negative is returned unchanged.
        self.assertEqual(absolute_value(4), 4)
        self.assertEqual(absolute_value(0), 0)

    def test_sign_and_absolute_value_next_to_zero(self):
        # Values right next to 0, including fractions.
        self.assertEqual(sign(1), 1)
        self.assertEqual(sign(-1), -1)
        self.assertEqual(absolute_value(-1), 1)
        self.assertEqual(absolute_value(0.5), 0.5)
        self.assertEqual(absolute_value(-0.5), 0.5)

    def test_max_of_two_when_first_is_larger(self):
        self.assertEqual(max_of_two(8, 3), 8)
        self.assertEqual(max_of_two(-1, -5), -1)

    def test_classify_temperature_boundaries(self):
        self.assertEqual(classify_temperature(14), "cold")
        self.assertEqual(classify_temperature(15), "warm")
        self.assertEqual(classify_temperature(24), "warm")
        self.assertEqual(classify_temperature(25), "hot")

    def test_grade_upper_edges_and_extremes(self):
        self.assertEqual(grade(100), "A")
        self.assertEqual(grade(89), "B")
        self.assertEqual(grade(79), "C")
        self.assertEqual(grade(69), "D")
        self.assertEqual(grade(0), "F")

    def test_single_if_without_else(self):
        self.assertEqual(clamp_to_limit(15, 10), 10)
        self.assertEqual(clamp_to_limit(5, 10), 5)
        self.assertEqual(clamp_to_limit(10, 10), 10)

    def test_compound_condition(self):
        self.assertIs(is_leap_year(2024), True)
        self.assertIs(is_leap_year(2023), False)
        self.assertIs(is_leap_year(1900), False)
        self.assertIs(is_leap_year(2000), True)

    def test_nested_if(self):
        self.assertEqual(ticket_price(17, False), 5)
        self.assertEqual(ticket_price(10, True), 5)
        self.assertEqual(ticket_price(18, True), 10)
        self.assertEqual(ticket_price(18, False), 20)

    def test_match_case(self):
        self.assertEqual(http_status(200), "OK")
        self.assertEqual(http_status(404), "Not Found")
        self.assertEqual(http_status(500), "Server Error")
        self.assertEqual(http_status(502), "Server Error")
        self.assertEqual(http_status(503), "Server Error")
        # The guard range includes both ends.
        self.assertEqual(http_status(400), "Client Error")
        self.assertEqual(http_status(403), "Client Error")
        self.assertEqual(http_status(499), "Client Error")
        self.assertEqual(http_status(399), "Unknown")
        self.assertEqual(http_status(301), "Unknown")
        self.assertEqual(http_status(504), "Unknown")
