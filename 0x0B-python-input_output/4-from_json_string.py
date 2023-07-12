#!/usr/bin/python3
"""
module doc
"""
import json


def from_json_string(my_str):
    """
    return an obj(Python data structure) represented by a JSON string.

    Args:
        my_str (str): JSON string to convert to an object.

    Returns:
        object: Python data structure rep by the JSON string.
    """
    return json.loads(my_str)
