#!/usr/bin/python3
"""a function that returns a list of lists of integers"""


def pascal_triangle(n):
    """a function that returns a list of lists of integers"""

    if n <= 0:
        return []

    triangle = []
    i = 0
    while i < n:
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)
        i += 1

    return triangle
