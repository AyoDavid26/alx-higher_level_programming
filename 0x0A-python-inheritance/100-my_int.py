#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """A class that inherits from int"""

    def __eq__(self, value):
        """turn the == to != or negator"""
        return self.real == value

    def __neg__(self, value):
        """Turning the != to =="""
        return self.__real == value
