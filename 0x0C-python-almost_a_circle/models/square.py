#!/usr/bin/python3
"""Module square.
Create a Square class, based on module rectangle"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes said square instance"""

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the str representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.__width)

    @property
    def size(self):
        """Sets the size of the Square."""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size attribute."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """updates the class Square by assigns attributes"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
