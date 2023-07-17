#!/usr/bin/python3
"""
module doc for Base
"""

class Base:
    """ the class manages id attribute """
    __nb_objects = 0
    def __init__(self, id=None):
        """ Initializes Base instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
