#!/usr/bin/python3
"""Defining a class to check function"""


def is_same_class(obj, a_class):
    """Checking if an object is an instance of a given class"""

    if type(obj) == a_class:
        return True
    return False
