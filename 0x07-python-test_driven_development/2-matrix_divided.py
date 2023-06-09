#!/usr/bin/python3
"""
A module that divides elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: The matrix containing integers or floats.
        div: The number to divide the matrix elements by.

    Returns:
        new_matrix: elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is equal to 0
        """
    """ Validate the matrix """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """ Validate the divisor """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    """ Divide the matrix elements and round to 2 decimal places """
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
