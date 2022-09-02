#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_list = []
        new_matrix.append(new_list)
        for j in i:
            new_list.append(j ** 2)

        return new_matrix
