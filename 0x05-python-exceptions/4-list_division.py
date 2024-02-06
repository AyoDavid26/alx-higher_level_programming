#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                division = 0
                if all(isinstance(i, (int,float)) for i in (my_list_1[i], my_list_2[i])):
                    if my_list_2[i] != 0:
                        division = my_list_1[i] / my_list_2[i]
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
