#!/usr/bin/python3
"""Defining a square"""


class Square():
    """Representation of a square"""

    def __init__(self, size=0):
        """ initializing the newly created square
        where: size equals size of the square and has default value 0
        """
        self.__size = size

        
    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """make the value of the set meet a standard"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public method to compute area of the class object"""
        return (self.__size * self.__size)

    def my_print(self):
        """Public instance method: that returns the current square area"""
        for item in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()
        if self.__size == 0:
            print()
