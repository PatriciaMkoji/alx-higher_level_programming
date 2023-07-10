#!/usr/bin/python3
"""
module doc
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialization of a Rectangle object with width and height.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcs area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns string representation of Rectangle object.

        Returns:
            str: string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
