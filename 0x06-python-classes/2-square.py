#!/usr/bin/python3
"""Defining a class Square"""


class Square():
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square
        where: size equates the size of squareand has a default value 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
