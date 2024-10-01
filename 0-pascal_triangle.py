#!/usr/bin/python3

"""
Returning a list of integers representing Pascal's triangle
"""


def pascal_triangle(n):

    if n <= 0:
        return []
    triangle = [[1]]
    for integer in range(1, n):
        row = [1]
        for k in range(1, integer):
            row.append(triangle[integer - 1][k - 1] + triangle[integer - 1][k])
        row.append(1)
        triangle.append(row)

    return triangle
