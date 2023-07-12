#!/usr/bin/python3
"""
module doc
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a txt file using a JSON representation.

    Args:
        my_obj (object): obj to be serialized & written to the file.
        filename (str): name of file to write the JSON representation to.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
