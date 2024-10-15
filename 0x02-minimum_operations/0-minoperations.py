#!/usr/bin/python3

""" 0x02. Minimum Operations
"""


def minOperations(n):
    """calculating operations
    """
    str = 'H'
    operations = 0
    factor = 2

    if n < 0:
        return 0

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor

        factor += 1

    return operations
