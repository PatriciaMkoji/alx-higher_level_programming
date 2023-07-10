#!/usr/bin/python3
"""
module doc
"""


class BaseGeometry:
    """
    A class that gives the basegeometry
    """

    def area(self):
        """
        calculates the area

        Args:
            self: calls itself

        Returns:
            area of basegeometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates integers

        Args:
            self: calls itself
            name: contains string
            value: checks if its greater than 0

        Returns:
            TypeError Exception: <name> must be integer
            ValueError Exception: <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
