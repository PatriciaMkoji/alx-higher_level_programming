#!/usr/bin/python3
""" Rectangle module"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle classinherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle instance

        Args:
            width: width of rectangle
            height: height of rectangle
            x: x-coordinate of rectangle
            y: y-coordinate of rectangle
            id: Id of instance(name)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get widthe """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ set height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x value """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y value """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ calc area """
        return (self.__height * self.__width)

    def display(self):
        """ display rectangle """
        myhash = "#"
        if self.width == 0 or self.height == 0:
            return
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end='')
            print(myhash * self.width)

    def update(self, *args, **kwargs):
        """ args Rectangle """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """ str format """
        st = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        st = st.format(self.id, self.x, self.y, self.width, self.height)
        return st

    def to_dictionary(self):
        """ dict of a rectangle """
        recdic = {"id": self.id, "width": self.width, "height": self.height,
                     "x": self.x, "y": self.y}
        return recdic
