#!/usr/bin/python3
"""Module square.
Create a Square class, based on module rectangle"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes said square instance"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

        @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
