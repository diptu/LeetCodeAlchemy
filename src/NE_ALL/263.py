"""
LeetCode #263. Ugly Number

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
An ugly number is a positive integer whose prime factors
are limited to 2, 3, and 5.

Given an integer `n`, return True if it is an ugly number,
otherwise return False.

Complexity
----------
Time  : O(log n)
Space : O(1)

Key Idea
--------
Repeatedly divide `n` by 2, 3, and 5 while divisible.
If the final result becomes 1 → it is an ugly number.
Otherwise → it contains other prime factors.
"""

from __future__ import annotations


class Solution:
    """Determine whether a number is an ugly number."""

    def isUgly(self, n: int) -> bool:  # noqa: N802
        if n <= 0:
            return False

        for factor in (2, 3, 5):
            while n % factor == 0:
                n //= factor

        return n == 1


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.isUgly(6) is True
    assert solution.isUgly(1) is True
    assert solution.isUgly(14) is False

    print("✅ All tests passed successfully!")
