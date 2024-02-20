#!/usr/bin/python3
"""defining a class student"""


class Student:
    """Representing a student"""

    def __init__(self, first_name, last_name, age):
        """Initializing students properties"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if(type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        for i, j in json.items():
            setattr(self, i, j)
