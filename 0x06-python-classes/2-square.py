#!/usr/bin/python3
"""a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Still defining the said square"""
    def __init__(self, size=0):
        """Instantiation of square"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
