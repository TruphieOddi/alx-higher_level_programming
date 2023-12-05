#!/usr/bin/python3
"""a class Student that defines a student by: (based on 9-student.py)"""


class Student:
    """Defines said student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = {}
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            for x in attrs:
                if hasattr(self, x):
                    my_dict[x] = getattr(self, x)
            return my_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance:"""

        for x in json:
            self.__dict__.update({x: json[x]})
