#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != None:
        for i in matrix:
            for j in range(len(matrix[i]):
                print("{:d}".format(matrix[j]), end="")
                if j < len(matrix[i]) - 1:
                    print(" ", end="")
            print()
