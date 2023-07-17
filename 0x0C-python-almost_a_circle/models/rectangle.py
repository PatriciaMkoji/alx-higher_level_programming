#!/usr/bin/python3
"""Rectangle module."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle instance.

        Args:
            width: width of rectangle
            height: height of rectangle
            x: x-coordinate of rectangle
            y: y-coordinate of rectangle
            id: Id of instance(name)
        """
        super().__init__(id)
        self.width = width
        self.heught = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """ get width """
            return self.__width

        @property
        def height(self):
            """ get height """
            return sef.__height

        @property
        def x(self):
            """ get x """
            return self.__x

        @property
        def y(self):
            """ get y """
            return self.__y

        @width.setter
        def width(self, value):
            """ set width """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @height.setter
        def height(self, value):
            """ set height value"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        @x.setter
        def x(self, value):
            """ set x value """
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @y.setter
        def y(self, value):
            """ set y value """
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise TypeError("y must be >= 0")
            self.__y = value
