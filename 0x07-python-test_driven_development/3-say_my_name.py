#!/usr/bin/python3
"""
module contains the 'say_my_name' function for printing a person's name
"""


def say_my_name(first_name, last_name=""):
    """
    prints a person's name <first_name> <last_name>

    Args:
    first_name (str): 1st name of the person.
    last_name (str, optional): The last name of the person

    Raises:
    TypeError: If first_name or last_name is not a string.

    Returns:
    None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
