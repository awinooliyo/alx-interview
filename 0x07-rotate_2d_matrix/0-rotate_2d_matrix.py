#!/usr/bin/python3
"""Rotating a 2-D Matrix in-place"""


def rotate rotate_2d_matrix(matrix):
    """
    Rotate a given n x n matrix 90 degrees
    clockwise in place.

    Parameters:
        matrix (list[list[int]]): the 2D matrix to be rotated.
    Returns:
        None.
    """
    n = len(matrix)
    n.reverse()
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
