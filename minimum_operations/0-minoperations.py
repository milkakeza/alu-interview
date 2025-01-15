#!/usr/bin/python3

"""
A script to calculate the fewest number of operations needed
to result in exactly n H characters in the file.
"""

def minOperations(n):


    """
    Calculate the minimum number of
    operations needed to achieve exactly `n` 'H' characters
    in a text file, starting with one 'H'.
    You can perform two operations: Copy All and Paste.

    Args:
    n (int): The target number of 'H' characters.
    Returns:
    int: The minimum number of 
    operations required to achieve `n` 'H' characters.
    """
    if n <= 1:
        return 0

    current = 1
    clipboard = current
    mN = 0

    while current < n:
        if n % current == 0:
            clipboard = current
            current = 2 * clipboard
            mN += 2
        else:
            current += clipboard
            mN += 1

    return mN
