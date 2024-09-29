#!/usr/bin/python3
"""Rotating a 2-D Matrix in-place"""


def rotate rotate_2d_matrix(matrix):
    """
    Rotate a given n x n matrix 90 degrees
    clockwise in place.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
