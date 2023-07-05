#!/usr/bin/python3
"""
    A module that adds 2 integers

    Args:
        a(int / float): 1st number
        b(int/ float): 2nd number. 98 is the default value

    Returns:
        sum of a and b typecasted to int
    Raises:
        TypeError: If a or b is not an integer or float
"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
