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

