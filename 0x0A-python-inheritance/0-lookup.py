#!/usr/bin/python3
def lookup(obj):
    """
    Module returns a list of available attributes & methods of an object

    Args:
        self: look into its own object

    Returns:
        listof attributes& methods of the object
    """
    return dir(obj)
