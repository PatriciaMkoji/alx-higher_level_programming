#!/usr/bin/python3
"""module that defines a class Square."""


class Square:
    """will represent a square."""

    def __init__(self, size):
        """Initialization of a new square.

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        retrieves the current size of the square.
        Returns:
            int: size of square
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
        """Returns current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character."""
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
