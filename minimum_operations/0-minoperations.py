#!/usr/bin/python3

def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve exactly `n` 'H' characters
    in a text file, starting with one 'H'. You can perform two operations: Copy All and Paste.

    Args:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required to achieve `n` 'H' characters.
    """

    if n <= 1:
        return 0

    operations = 0

    while n > 1:
        if n % 3 == 0:
            n //= 3
        else:
            n -= 1

        operations += 1

    return operations
