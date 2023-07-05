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

    new_text = ""
    for char in text:
        if char in ['.', '?', ':']:
            new_text += char + "\n\n"
        else:
            new_text += char
    lines = new_text.splitlines()
    for line in lines:
        print(line.strip())
