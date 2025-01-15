#!/usr/bin/python3

"""
A script to calculate the fewest number of operations needed
to result in exactly n H characters in the file.
"""

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

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = 1 + min(dp[i - 1], dp[i // 2] + i % 2)

    return dp[n]
