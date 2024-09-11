#!/usr/bin/python3
"""
This module provides a function that calculates the minimum number of operations."""


def minOperations(n):
    """
    Calculates the minimum number of operations to get exactly n 'H' characters."""

   """ Args:
        n (int): The number of 'H' characters to achieve.
   """
   """ Returns:
        int: The fewest number of operations required, or 0 if it's impossible.
    """
    # Impossible cases: when n is 0 or negative
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Iteratively reduce n by its factors, counting operations
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
