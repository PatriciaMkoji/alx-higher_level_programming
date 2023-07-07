#!/usr/bin/python3
"""
A module that indents a text
"""


def text_indentation(text):
    """
    the func prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text (str): input text.

    Raises:
    TypeError: when text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    new_text = text
    for char in delimiters:
        new_text = new_text.replace(char, char + '\n')

    lines = new_text.split('\n')
    for line in lines:
        print(line.strip())
