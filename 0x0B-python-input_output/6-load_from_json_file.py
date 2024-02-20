#!/usr/bin/python3
"""to load from a json file"""
import json


def load_from_json_file(filename):
    """
    A function that creates an object from a json file
    """

    with open(filename, encoding='utf-8') as file_loaded:
        return json.load(file_loaded)
