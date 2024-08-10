#!/usr/bin/python3
"""0-minoperations module"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters.
    Args:
        n: The desired number of H characters.
    Returns:
        An integer representing the minimum number of operations,
        or 0 if n is impossible to achieve.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
