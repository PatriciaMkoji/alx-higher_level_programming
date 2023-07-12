#!/usr/bin/python3
"""
module doc
"""


class Student:
    """
    Class rep a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): The age of the student.
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
            dict: The dict rep of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr
                    in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of student instance using a dict rep

        Args:
            json (dict): Dict rep containing attribute-value pairs.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
