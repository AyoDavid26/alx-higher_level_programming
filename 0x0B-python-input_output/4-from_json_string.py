#!/usr/bin/python3
"""function that represents a json string"""


import json


def from_json_string(my_str):
    """returning an object represented by a json string"""

    return json.loads(my_str)
