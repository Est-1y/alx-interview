#!/usr/bin/python3

"""
Returning a list of integers representing Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns a list of numbers
    """
    m = []
    if n <= 0:
        return m
    m = [[1]]
    for i in range(1, n):
        temp = [1]
        for k in range(len(m[i - 1]) - 1):
            curr = m[i - 1]
            temp.append(m[i - 1][k] + m[i - 1][j + 1])
        temp.append(1)
        m.append(temp)
    return m
