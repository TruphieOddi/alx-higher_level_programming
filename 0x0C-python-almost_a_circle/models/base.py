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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
                not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
