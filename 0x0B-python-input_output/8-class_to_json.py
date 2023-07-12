#!/usr/bin/python3
"""
module doc
"""


def class_to_json(obj):
    """
    Returns dict descptn with a simple datastruct 4 JSON serizn of an obj

    Args:
        obj: An instance of a class.

    Returns:
        dict: dictionary description with a simple data structure.

    """
    return obj.__dict__
