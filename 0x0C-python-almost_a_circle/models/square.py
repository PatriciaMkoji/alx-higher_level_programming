#!/usr/bin/python3
""" Squeare module """

from models.rectangle import Rectangle

class Square(Rectangle):
    """square inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialzation of square

        Args:
            size: size os square, width & height
            x: x coordinate of square
            y: yy coordinate of square
            id: idinstance(unique name)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, value):
        """ set size value """
        self.width = value
        self.height = value

    def __str(self):
        """ print Method """
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        s = s.format(self.id, self.x, self.y, self.width)
        return s

    def update(self, *args, **kwargs):
        """ update square """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j

            else:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    self.size = kwargs["size"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """dict square """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
