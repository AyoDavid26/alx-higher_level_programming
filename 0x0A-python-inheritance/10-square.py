#!/usr/bin/python3
"""Importing base class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from base class rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size * self.__size
