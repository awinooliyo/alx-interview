#!/usr/bin/python3
"""A script that determines the Pascal's triangle for any number"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's
    triangle of n
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:  # Corrected condition here
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)
    return triangle
