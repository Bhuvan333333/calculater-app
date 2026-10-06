"""Core calculator operations for two positive integers."""


def _validate(a, b):
    for value in (a, b):
        # bool is a subclass of int, so reject it explicitly
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"Expected a positive integer, got {value!r}")
        if value <= 0:
            raise ValueError(f"Expected a positive integer, got {value}")


def add(a: int, b: int) -> int:
    _validate(a, b)
    return a + b


def subtract(a: int, b: int) -> int:
    _validate(a, b)
    return a - b


def multiply(a: int, b: int) -> int:
    _validate(a, b)
    return a * b
