#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = [new[:] for new in matrix]
    for idx, new in enumerate(my_matrix):
        for idx2, col in enumerate(my_matrix):
            my_matrix[idx][idx2] = new[idx2] ** 2
    return my_matrix
