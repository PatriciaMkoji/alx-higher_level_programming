#!/usr/bin/python3
"""module that defines a class Square."""


class Square:
    """will represent a square."""

    def __init__(self, size=0):
        """
        Initialization of a new square.

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        will retrieve the size of the square.
        Returns:
             int: size of sqaure
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current area of the square.
        Returns:
            int: area
        """
        return (self.__size * self.__size)
