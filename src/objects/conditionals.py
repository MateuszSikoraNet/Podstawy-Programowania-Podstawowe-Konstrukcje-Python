class Classifier:
    def sign(self, value):
        # Return -1, 0, or 1 based on value.
        pass

    def absolute_value(self, value):
        # Return value without its sign.
        pass

    def max_of_two(self, a, b):
        # Return the larger value.
        pass

    def grade(self, score):
        # Return A for scores of 90 or more.
        # Return B for scores of 80 or more.
        # Return C for scores of 70 or more.
        # Return D for scores of 60 or more.
        # Return F for lower scores.
        pass

    def fizz_buzz(self, value):
        # Return FizzBuzz for multiples of 3 and 5.
        # Return Fizz for multiples of 3.
        # Return Buzz for multiples of 5.
        # Return the value otherwise.
        pass

    def classify_temperature(self, temperature):
        # Return cold below 15, warm from 15 to below 25, hot from 25 up.
        pass

    def clamp_to_limit(self, value, limit):
        # If value is greater than limit, replace it with limit. Return value.
        # A single if without else - nothing happens when the condition is False.
        pass

    def is_leap_year(self, year):
        # Return True for years divisible by 4, except years divisible by 100 that are not divisible by 400.
        # Use one condition combining and/or/not.
        pass

    def ticket_price(self, age, is_student):
        # Return 5 for age below 18. Otherwise check is_student inside that branch (nested if):
        # return 10 for students and 20 for everyone else.
        pass

    def http_status(self, code):
        # Use match/case: 200 -> "OK", 404 -> "Not Found", 500 | 502 | 503 -> "Server Error",
        # any other code from 400 to 499 -> "Client Error" (a case with a guard: case c if ...),
        # anything else -> "Unknown" (the wildcard case _).
        pass
