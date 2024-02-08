#!/usr/bin/python3
"""Defining a square"""


class Square():
    """Representing a square"""

    def __init__(self, size=0):
        """ initialize the newly created square
        where: size equals the size of the square and has default value 0
        """
        self.__size = size

    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public method to compute area of the class object"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """define the == comparison of a square area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """define the != comparison with a square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """define the < comparison with a square"""
        return self.area() < other.area()

    def __le__(self, other):
        """define the <= comparison with a square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """define the > comparison with a square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """define the >= comparison with a square"""
        return self.area() >= other.area()
