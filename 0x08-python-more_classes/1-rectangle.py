#!/usr/bin/python3
"""To define a rectangle class"""


class Rectangle:
    """Representing a rectangle"""

    def __init__(self, width=0, height=0):
        """To initialize a newly created rectangle.

        where:
        width (int): width of the newly created rectangle.
        height (int): height of the newly created rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
