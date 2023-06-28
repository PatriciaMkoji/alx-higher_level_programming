#!/usr/bin/python3
"""module that defines a class Square."""


class Square:
    """will represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization a new square.

        Args:
            size (int): size of the new square.
            position (int, int): position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        retrives the current size of the square.
        Returns:
             int: size od sq
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrives the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """will print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            print("")
