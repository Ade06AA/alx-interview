#!/usr/bin/python3
"""
doc
"""


def pascal_triangle(n):
    """
    pascal triamgle
    """
    triangle = []
    if n < 1:
        return triangle
    triangle.append([1])
    for i in range(2, n+1):
        new = []
        for j in range(len(triangle[-1])):
            if j == 0:
                new.append(1)
            else:
                new.append(triangle[-1][j] + triangle[-1][j - 1])

            if j == len(triangle[-1]) - 1:
                new.append(1)
        triangle.append(new)
    return triangle
