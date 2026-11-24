import unittest

from src.objects.conditionals import Classifier


class TestClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = Classifier()

    def test_sign_and_absolute_value(self):
        self.assertEqual(self.classifier.sign(-4), -1)
        self.assertEqual(self.classifier.sign(0), 0)
        self.assertEqual(self.classifier.sign(4), 1)
        self.assertEqual(self.classifier.absolute_value(-4), 4)

    def test_max_of_two(self):
        self.assertEqual(self.classifier.max_of_two(3, 8), 8)
        self.assertEqual(self.classifier.max_of_two(5, 5), 5)

    def test_grade_boundaries(self):
        self.assertEqual(self.classifier.grade(90), "A")
        self.assertEqual(self.classifier.grade(80), "B")
        self.assertEqual(self.classifier.grade(70), "C")
        self.assertEqual(self.classifier.grade(60), "D")
        self.assertEqual(self.classifier.grade(59), "F")

    def test_fizz_buzz(self):
        self.assertEqual(self.classifier.fizz_buzz(3), "Fizz")
        self.assertEqual(self.classifier.fizz_buzz(5), "Buzz")
        self.assertEqual(self.classifier.fizz_buzz(15), "FizzBuzz")
        self.assertEqual(self.classifier.fizz_buzz(7), 7)

    def test_classify_temperature(self):
        self.assertEqual(self.classifier.classify_temperature(10), "cold")
        self.assertEqual(self.classifier.classify_temperature(20), "warm")
        self.assertEqual(self.classifier.classify_temperature(30), "hot")

    def test_absolute_value_of_non_negative_is_unchanged(self):
        # A value that is not negative is returned unchanged.
        self.assertEqual(self.classifier.absolute_value(4), 4)
        self.assertEqual(self.classifier.absolute_value(0), 0)

    def test_sign_and_absolute_value_next_to_zero(self):
        # Values right next to 0, including fractions.
        self.assertEqual(self.classifier.sign(1), 1)
        self.assertEqual(self.classifier.sign(-1), -1)
        self.assertEqual(self.classifier.absolute_value(-1), 1)
        self.assertEqual(self.classifier.absolute_value(0.5), 0.5)
        self.assertEqual(self.classifier.absolute_value(-0.5), 0.5)

    def test_max_of_two_when_first_is_larger(self):
        self.assertEqual(self.classifier.max_of_two(8, 3), 8)
        self.assertEqual(self.classifier.max_of_two(-1, -5), -1)

    def test_classify_temperature_boundaries(self):
        self.assertEqual(self.classifier.classify_temperature(14), "cold")
        self.assertEqual(self.classifier.classify_temperature(15), "warm")
        self.assertEqual(self.classifier.classify_temperature(24), "warm")
        self.assertEqual(self.classifier.classify_temperature(25), "hot")

    def test_grade_upper_edges_and_extremes(self):
        self.assertEqual(self.classifier.grade(100), "A")
        self.assertEqual(self.classifier.grade(89), "B")
        self.assertEqual(self.classifier.grade(79), "C")
        self.assertEqual(self.classifier.grade(69), "D")
        self.assertEqual(self.classifier.grade(0), "F")

    def test_single_if_without_else(self):
        self.assertEqual(self.classifier.clamp_to_limit(15, 10), 10)
        self.assertEqual(self.classifier.clamp_to_limit(5, 10), 5)
        self.assertEqual(self.classifier.clamp_to_limit(10, 10), 10)

    def test_compound_condition(self):
        self.assertIs(self.classifier.is_leap_year(2024), True)
        self.assertIs(self.classifier.is_leap_year(2023), False)
        self.assertIs(self.classifier.is_leap_year(1900), False)
        self.assertIs(self.classifier.is_leap_year(2000), True)

    def test_nested_if(self):
        self.assertEqual(self.classifier.ticket_price(17, False), 5)
        self.assertEqual(self.classifier.ticket_price(10, True), 5)
        self.assertEqual(self.classifier.ticket_price(18, True), 10)
        self.assertEqual(self.classifier.ticket_price(18, False), 20)

    def test_match_case(self):
        self.assertEqual(self.classifier.http_status(200), "OK")
        self.assertEqual(self.classifier.http_status(404), "Not Found")
        self.assertEqual(self.classifier.http_status(500), "Server Error")
        self.assertEqual(self.classifier.http_status(502), "Server Error")
        self.assertEqual(self.classifier.http_status(503), "Server Error")
        # The guard range includes both ends.
        self.assertEqual(self.classifier.http_status(400), "Client Error")
        self.assertEqual(self.classifier.http_status(403), "Client Error")
        self.assertEqual(self.classifier.http_status(499), "Client Error")
        self.assertEqual(self.classifier.http_status(399), "Unknown")
        self.assertEqual(self.classifier.http_status(301), "Unknown")
        self.assertEqual(self.classifier.http_status(504), "Unknown")
