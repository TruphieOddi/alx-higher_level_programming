#!/usr/bin/python3
"""Module base that defines a base model class"""


import json
import os
import csv


class Base:
    """This is the base for the incoming tasks with private class attribute:
    __nb_objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a Base instance."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
