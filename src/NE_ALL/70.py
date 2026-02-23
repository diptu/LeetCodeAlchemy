"""
LeetCode #70. Climbing Stairs

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
You are climbing a staircase with `n` steps.
Each time you can climb either 1 or 2 steps.

Return the number of distinct ways to reach the top.

Complexity
----------
Time  : O(n)
Space : O(1)

Key Idea
--------
This is a Fibonacci-type DP problem.

Let:
    dp[i] = number of ways to reach step i

Recurrence:
    dp[i] = dp[i - 1] + dp[i - 2]

We optimize space by keeping only the last two values.
"""

from __future__ import annotations


class Solution:
    """Return number of distinct ways to climb n stairs."""

    def climbStairs(self, n: int) -> int:  # noqa: N802
        if n <= 2:
            return n

        prev_two: int = 1  # dp[i - 2]
        prev_one: int = 2  # dp[i - 1]

        for _ in range(2, n):
            current = prev_one + prev_two
            prev_two = prev_one
            prev_one = current

        return prev_one


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
    assert solution.climbStairs(5) == 8

    print("✅ All tests passed successfully!")
