#!/usr/bin/python3
"""
module doc
"""
import json


def to_json_string(my_obj):
    """
    Return JSON representation of an object (string).

    Args:
        my_obj (object): object to convert to JSON.

    Returns:
        str: JSON representation of obj
    """
    return json.dumps(my_obj)
