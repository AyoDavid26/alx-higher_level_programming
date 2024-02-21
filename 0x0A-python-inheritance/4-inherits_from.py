#!/usr/bin/python3
"""Defining a class that inherited directly or
indirectly from another class"""


def inherits_from(obj, a_class):
    """Checking if an object is an inherited instance of a class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
