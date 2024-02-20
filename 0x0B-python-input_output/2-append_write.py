#!/usr/bin/python3
"""Defining how a module appends a string at end of a text file"""


def append_write(filename="", text=""):
    """Appending a string to the end of a UTF-8 text file"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
