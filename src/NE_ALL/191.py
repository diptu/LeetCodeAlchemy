"""
LeetCode #191. Number of 1 Bits

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given an integer `n`, return the number of '1' bits
(also known as the Hamming weight).

Complexity
----------
Time  : O(k), where k = number of set bits
Space : O(1)

Key Idea
--------
Use Brian Kernighan’s Algorithm:

- Repeatedly remove the lowest set bit using:
      n = n & (n - 1)
- Each operation removes one '1' bit
- Count how many times this operation runs
"""

from __future__ import annotations


class Solution:
    """Count number of set bits in an integer."""

    def hammingWeight(self, n: int) -> int:  # noqa: N802
        count: int = 0

        while n:
            n &= n - 1
            count += 1

        return count


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.hammingWeight(11) == 3  # 1011
    assert solution.hammingWeight(2147483645) == 30
    assert solution.hammingWeight(128) == 1  # 10000000

    print("✅ All tests passed successfully!")
