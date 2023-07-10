#!/usr/bin/python3
"""
module doc
"""


def add_attribute(obj, name, value):
    """
        module adds a new attribute to object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
