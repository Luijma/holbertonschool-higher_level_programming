#!/usr/bin/python3
""" matrix_divided module """


def matrix_divided(matrix, div):
    """ Divides all elemets in a matrix
    Args:
        matrix (list): matrix to be divided
        div (Union[int, float]): number to be divided
    """
    is_correct_type = False
    new_matrix = [i[:] for i in matrix]
    if all(isinstance(ele, list) for ele in new_matrix) is True:
        is_correct_type = True
        for row in range(len(new_matrix)):
            for column in range(len(matrix[row])):
                if (type(new_matrix[row][column]) != int and
                        type(new_matrix[row][column]) != float):
                    is_correct_type = False
                    break
            if (is_correct_type is False):
                break
    if(is_correct_type is False):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    new_matrix = [[round(i / div, 2) for i in j] for j in new_matrix]
    return new_matrix
    """ returns a new matrix with new values """
