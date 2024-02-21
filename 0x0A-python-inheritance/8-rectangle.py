#!/usr/bin/python3
"""A new class based on 7-base_geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing a class that inherits from Base Geometry"""
    def __init__(self, width, height):
        """instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
