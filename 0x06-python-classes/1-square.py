#!/usr/bin/python3
"""a class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """
    Definition of the above class square

    Attributes:
        size: sq size.
    """
    def __init__(self, size):
        """Instantiation with size (no type/value verification)"""
        self.__size = size
