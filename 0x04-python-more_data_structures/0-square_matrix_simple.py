#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def squares(sq):
        return sq * sq
    new_matrix = []
    for row in matrix:
        new_row = list(map(squares, row))
        new_matrix.append(new_row)
    return new_matrix
