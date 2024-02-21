#!/usr/bin/python3
"""Defining a class MyList"""


class MyList(list):
    """Representing MyList"""

    def print_sorted(self):
        """Prints a sorted list"""

        print(sorted(self))
