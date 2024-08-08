#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to result in exactly n H
"""


def minOperations(n):
    """
    Returns an interger
    returns 0 if fail
    """
    operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations
