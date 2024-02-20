#!/usr/bin/python3
"""Function that writes string to text file"""


def write_file(filename="", text=""):
    """To write a string to a UTF-8 text file.
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(text)
