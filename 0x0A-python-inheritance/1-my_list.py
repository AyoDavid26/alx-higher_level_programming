#!/usr/bin/python3
"""Defining a class MyList"""


class MyList(list):
    """Representing class MyList that takes base class as argument"""
    def print_sorted(self):
        """Fucntion defination to Print a sorted list"""
        print(sorted(self))
