#!/usr/bin/python3

"""Defining a class square"""


class Square():
    """Representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing new square
        where: size equals the size of the new square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """To get size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Private instance attribute: position"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter def position(self, value): to set it"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public method to compute area of a class object"""
        return (self.__size * self.__size)

    def my_print(self):
        """to print the square with #"""
        for i in range(0, self.__size):
            [print('#', end="") for j in range(self.__size)]
            print("")
            if self.__size == 0:
                print("")
