#!/usr/bin/python3

"""Defining a class Square"""

class Square:
    """Representing a square"""

    def __init__(self, size=0):
        """Initializing a newly created square
        where: size equals the size of new square.
        """

    @property
    def size(self):
        """to get the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public method to compute area of the class object"""
        return (self.__size * self.__size)
