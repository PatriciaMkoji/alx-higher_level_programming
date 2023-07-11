#!/usr/bin/python3
"""
module doc
"""


def read_file(filename=""):
    """
    function that reads a text file and prints it out

    Args:
        filenme: file to be read

    Return:
        printed out text
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
