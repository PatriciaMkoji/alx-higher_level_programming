#!/usr/bin/python3
"""
module doc
"""
import json


def load_from_json_file(filename):
    """
    Create an obj from a JSON file.

    Args:
        filename (str): name of the JSON file to load the object from.

    Returns:
        object: Python object created from the JSON data.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
