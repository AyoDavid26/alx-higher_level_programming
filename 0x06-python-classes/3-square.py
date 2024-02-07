#!/usr/bin/python3
"""Defining a square"""

class Square():
    """Representation of a square"""

    def __init__(self, size=0):
        """initialize the new square
        where: size equals the size of the square and has default value 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """a public method to compute the area of the class object"""

        return (self.__size * self.__size)
