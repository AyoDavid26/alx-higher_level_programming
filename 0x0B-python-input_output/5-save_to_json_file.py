#!/usr/bin/python3
"""defining save_to_json_file module"""

import json


def save_to_json_file(my_obj, filename):
    """a function that writes an object to text file"""

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False)
