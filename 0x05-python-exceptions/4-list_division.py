#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for items in range (list_length):
            try:
                division = 0
                if isinstance(my_list_1[items], (int, float)) and isinstance(my_list_2[items], (int, float)):
                    if my_list_2[items] != 0:
                        division = my_list_1[items] / my_list_2[items]
                    else:
                        print("division by 0")
                else:
                    print("wrong type")
            except IndexError:
                print("out of range")
            finally:
                result.append(division)
    finally:
        return result
