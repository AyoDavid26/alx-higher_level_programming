#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    updated_list = my_list[:]
    for idx, c in enumerate(updated_list):
        if c == search:
            updated_list[idx] = replace
    return updated_list
