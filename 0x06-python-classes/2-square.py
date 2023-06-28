#!/usr/bin/python3

"""
the module defines a Square class.
"""


class Square:
    """
    it represents a square.
    """


    def __init__(self, size=0):
        """
        Initialization of a Square instance.

        Args:
            size (int): size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

