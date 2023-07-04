#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        text_indent += char
        if char == '.'or char == '?' or char == ':':
            text_indent += "\n\n"
        print("\n{}".format(text))
