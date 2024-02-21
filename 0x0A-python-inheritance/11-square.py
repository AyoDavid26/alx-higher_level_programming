#!/usr/bin/python3
"""Importing a base class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square that inherits from a base class Rectangle"""
    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size * self.__size
