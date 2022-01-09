#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [i[:] for i in matrix]
    new_matrix = [[i ** 2 for i in j] for j in new_matrix]
    return new_matrix
