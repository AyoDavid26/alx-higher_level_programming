#!/usr/bin/python3
"""Defining a class that's inherited froma nother class"""


def is_kind_of_class(obj, a_class):
    """Checking if object is an instance of inherited instance or class"""

    if isinstance (obj, a_class):
        return True
    return False
