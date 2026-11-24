def safe_divide(a, b, default=None):
    # Divide a by b.
    # Return the default if b is zero.
    pass


def parse_int(value, default=None):
    # Convert value to an integer.
    # Return the default if conversion fails.
    pass


def get_element(values, index):
    # Return the value at index.
    pass


def safe_get(mapping, key, default=None):
    # Return the default if key is not in mapping.
    pass


def validate_age(age):
    # Raise ValueError if age is below 0 or above 120.
    # Return True for a valid age.
    pass


def divide_report(a, b):
    # Return the list of blocks that ran, in order, for:
    # try: a / b  ->  except ZeroDivisionError  ->  else (only when no error)  ->  finally (always).
    # Append "try", "except", "else" and "finally" to the list inside those blocks.
    pass


def convert_with_log(value, log):
    # try: return int(value)  finally: log.append("closed")
    # No except: a ValueError leaves the function, but finally still runs first.
    pass


def describe_error(value):
    # Try int(value). On ValueError return "Error: " + the error message (except ValueError as error: str(error)).
    # Return "OK" when there is no error.
    pass


def load_setting(settings, key):
    # Return settings[key]. If the key is missing, raise ValueError(f"Missing setting: {key}")
    # from the original KeyError (except KeyError as error: raise ValueError(...) from error).
    pass


def parse_or_log(text, log):
    # Return int(text). If it fails, append text to log and re-raise the same error with a bare "raise".
    pass


def check_positive(value):
    # assert value > 0, "value must be positive"  - then return value.
    # A failed assert raises AssertionError. Asserts are for programmer mistakes, not user input
    # (python -O turns them off).
    pass


def lookup(container, key, default=None):
    # Return container[key], or default if it fails with IndexError (list) or KeyError (dict).
    # Catch both at once with their common parent class: except LookupError.
    # Other errors (e.g. TypeError for a list with a str key) must not be caught.
    pass


def convert_status(value):
    # Try int(value) and return "ok". Use two separate except blocks:
    # except ValueError -> return "bad value" (e.g. "abc"), except TypeError -> return "bad type" (e.g. None, [1]).
    pass


def classify_lookup(container, key):
    # Return container[key] if it works. Otherwise use two except blocks:
    # except KeyError -> return "missing key", except LookupError -> return "lookup failed".
    # Order matters: Python uses the first matching block, so the more specific KeyError must come first
    # (with LookupError first, the KeyError block would never run).
    pass
