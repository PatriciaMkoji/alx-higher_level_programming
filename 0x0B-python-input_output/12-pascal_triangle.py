#!/usr/bn/python3
"""
module doc
"""


def pascal_triangle(n):
    """
    it generates Pascal's triangle of size n.

    Args:
        n (int): size of the Pascal's triangle.

    Returns:
        list: this list of lists representing Pascal's triangle.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
