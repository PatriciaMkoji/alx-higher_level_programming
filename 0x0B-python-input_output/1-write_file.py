#!/usr/bin/python3
"""
module doc
"""
def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)& return the num of chars written.

    Args:
        filename (str): name of the file to write to.
        text (str): text to write to the file.

    Returns:
        int: number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)

