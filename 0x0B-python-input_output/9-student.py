#!/usr/bin/python3
"""
module doc
"""


class Student:
    """
    the class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialization of a Student instance.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary rep of a Student instance.

        Returns:
            dict: dict rep of the student.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
