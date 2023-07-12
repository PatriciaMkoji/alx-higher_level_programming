#!/usr/bin/python3
"""
module doc
"""


def append_write(filename="", text=""):
    """
    append a string at the end file (UTF8) & return the num of chars added.

    Args:
        filename (str): name of the file to append to.
        text (str): text to append to the file.

    Returns:
        int: number of char added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
