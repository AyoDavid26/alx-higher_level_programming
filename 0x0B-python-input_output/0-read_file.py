#!/usr/bin/python3

"""Defining a read file module"""


def read_file(filename=""):
    """
    reading a file function
    to read a text file (UTF-8) and print the result to stdout
    """

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
