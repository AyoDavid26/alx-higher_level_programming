#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        update1 = my_string.translate({ord("c"): None})
        update2 = update1.translate({ord("C"): None})
        return update2
    return my_string
