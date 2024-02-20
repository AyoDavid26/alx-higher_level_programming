#!/usr/bin/python3
"""Appending after module"""


def append_after(filename="", search_string="", new_string=""):
    """class body
    """
    text = ""
    with open(filename) as read:
        for line in read:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
