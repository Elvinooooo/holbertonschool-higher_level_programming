#!/usr/bin/python3
"""Define an integer addition function."""


def add_integer(a, b=98):
    """Return the addition of a and b.

    Float arguments are converted to ints before addition is performed.

    Raises:
        TypeError: If either  a or b is a non-integer and non-float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
