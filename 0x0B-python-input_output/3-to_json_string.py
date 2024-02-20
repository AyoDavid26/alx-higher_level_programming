#!/usr/bin/python3
"""Defining to_json_string modules"""


import json


def to_json_string(my_obj):
    """to return the JSON representation of an object"""

    return json.dumps(my_obj)
