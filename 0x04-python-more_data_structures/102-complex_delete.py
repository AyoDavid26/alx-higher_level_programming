#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    [a_dictionary.pop(k) for k, v in list(a_dictionary.items()) if v == value]
    return a_dictionary
