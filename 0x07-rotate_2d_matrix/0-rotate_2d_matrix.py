#!/usr/bin/env python3
"""0-rotate_2d_matrix module"""


def rotate_2d_matrix(matrix):
    """rotates a 2D matrix by 90 degrees clockwise"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
