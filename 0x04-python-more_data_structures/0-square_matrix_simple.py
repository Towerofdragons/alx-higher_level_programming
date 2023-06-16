#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        res = []
        for col in row:
            res.append(col ** 2)
        new_matrix.append(res)
    return new_matrix
