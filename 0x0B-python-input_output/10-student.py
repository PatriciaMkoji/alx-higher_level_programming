#!/usr/bin/python3
"""
module doc
"""


class Student:
    """
    rep a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dict rep of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve (default: None).

        Returns:
            dict: dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
