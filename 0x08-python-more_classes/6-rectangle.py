#!/usr/bin/python3

"""
A rectangle module
"""


class Rectangle:
    """
    a class rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ gets the width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width of the rectangle. """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height of the rectangle """

        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ calcs the perimeter of rectangle """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ returns the string represantationof rect """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """ string represantatio of the rect """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ when instance of a rectangle is deleted, a message is printed """
        print("Bye rectangle...")
