#!/usr/bin/env python3

"""
Calculate the minimum number of operations to reach exactly 'n' characters.
"""

def min_operations(n):
    """
    Determines the minimum number of operations required to reach 'n' characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations needed.
    """
    # Handle edge cases for small n values
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n //= divisor
            operations += divisor
        divisor += 1
        
    return operations
