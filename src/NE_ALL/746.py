"""
LeetCode #746. Min Cost Climbing Stairs

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
You are given an integer array `cost` where `cost[i]` is the cost
of stepping on the i-th stair.

You can start from step 0 or step 1.
Each time you can climb either 1 or 2 steps.

Return the minimum cost to reach the top of the floor.

Complexity
----------
Time  : O(n)
Space : O(n)

Key Idea
--------
Dynamic Programming.

Let:
    dp[i] = minimum cost to reach step i

Recurrence:
    dp[i] = min(
        cost[i-1] + dp[i-1],
        cost[i-2] + dp[i-2]
    )

We build the solution bottom-up.
"""

from __future__ import annotations
from typing import List


class Solution:
    """Compute the minimum cost to reach the top of the stairs."""

    def minCostClimbingStairs(self, cost: List[int]) -> int:  # noqa: N802
        n: int = len(cost)
        dp: List[int] = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(
                cost[i - 1] + dp[i - 1],
                cost[i - 2] + dp[i - 2],
            )

        return dp[n]


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.minCostClimbingStairs([10, 15, 20]) == 15
    assert solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

    print("✅ All tests passed successfully!")
