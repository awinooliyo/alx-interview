#!/usr/bin/env python3
"""

"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n 'H' characters in the file.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required,
    or 0 if it's impossible to achieve n characters.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
