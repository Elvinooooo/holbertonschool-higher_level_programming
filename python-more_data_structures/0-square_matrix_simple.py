#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rows in matrix:
        new_array = []
        for colums in rows:
            new_array.append(colums**2)
        new_matrix.append(new_array)
    return new_matrix
