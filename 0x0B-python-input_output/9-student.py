#!/usr/bin/python3
"""defining a class student"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initializing student details in constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            return self.__dict__
