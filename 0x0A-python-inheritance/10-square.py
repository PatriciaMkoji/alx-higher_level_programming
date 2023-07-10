#!/usr/bin/python3
"""
    square class module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square Class inherits other class
    """
    def __init__(self, size):
        """
            Initialization of square
        """
        self.__size = size
        self.integer_validator('size', self.__size)

    def area(self):
        """
        area defination
        """
        return self.__size ** 2

    def __str__(self):
        """
            implementation of __str__
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
