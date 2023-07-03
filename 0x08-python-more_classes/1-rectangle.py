#!/usr/bin/python3
"""
A module rectangle
"""


class Rectangle:
    """
    A function that initializes a rectangle

    Args:
    width: width of rectangle
    height: height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get width of rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """ set width ogf rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """ get height of triangle """
        return self._height

    @height.setter
    def height(self, value):
        """ set the height of triangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
