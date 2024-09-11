#!/usr/bin/python3

def minOperations(n):
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
