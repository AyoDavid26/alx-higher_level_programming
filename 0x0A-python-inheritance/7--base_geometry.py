#!/usr/bin/python3
"""Defining a new class based on 6-base_geometry"""


class BaseGeometry:
    """a class that is meant to be a base class"""
    def are(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
