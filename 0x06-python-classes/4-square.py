#!/usr/bin/python3
"""a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """still defining the same square class"""
    def __init__(self, size=0):
        """Creates new instances of sq"""
        self.__size = size

    def area(self):
        """Calculates area of said square"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns property size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method used"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
