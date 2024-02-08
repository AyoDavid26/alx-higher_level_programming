#!/usr/bin/python3

"""MagicClass object which uses a math func.
so we use import math
"""
import math


class MagicClass:
    def __init__(self, radius=0):
        """initializing the magic class with radius as param"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """To compute the area of the circle"""

        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """to compute the circumference of a circle"""
        return (2 * math.pi * self.__radius)
