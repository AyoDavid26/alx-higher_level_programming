#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for q in sorted(a_dictionary.keys()):
        print("{}: {}".format(q, a_dictionary.get(q)))
