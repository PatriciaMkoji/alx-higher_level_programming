#!/usr/bin/python3
"""
Module doc
"""


def is_same_class(obj, a_class):
    """
    checks if the object is exactly as the instance of the specified class

    Args:
        obj: on]bject to be checked
        a_class: class to be compared

    Returns:
        True: is the same
        False: not the same
    """
    return isinstance(obj, a_class)
