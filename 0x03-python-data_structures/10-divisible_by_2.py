#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = len(my_list)
    updated_list = []
    for a in range(i):
        if my_list[a] % 2 == 0:
            updated_list.append(True)
        else:
            updated_list.append(False)
    return updated_list
