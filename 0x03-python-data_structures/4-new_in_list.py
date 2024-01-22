#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    all_list = my_list[:]
    if idx < 0:
        return all_list
    if idx > len(my_list) - 1:
        return all_list
    all_list[idx] = element
    return all_list
