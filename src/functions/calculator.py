def add(a: float, b: float) -> float:
    # Use `+` operator.
    return a + b


def subtract(a: float, b: float) -> float:
    # Use `-` operator.
    return a - b


def multiply(a: float, b: float) -> float:
    # Use `*` operator.
    return a * b


def divide(a: float, b: float) -> float:
    # Raise ValueError exception if b is 0.
    if b == 0:
        raise ValueError("Cannot divide by zero")

    # Use `/` operator.
    return a / b
