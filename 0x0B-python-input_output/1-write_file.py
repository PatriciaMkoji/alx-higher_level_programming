#!/usr/bin/ptyhon3
"""
module docu
"""


def write_file(filename="", text=""):
    """
    function writes a string totextfile(UTF8) & returns the No: of chars

    Args:
        filename: file to be written

    text:
        text to be written on file

    Returns:
        No of chars
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
