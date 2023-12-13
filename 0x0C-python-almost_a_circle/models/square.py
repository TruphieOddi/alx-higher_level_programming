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
