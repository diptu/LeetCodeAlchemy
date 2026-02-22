"""
LeetCode #198. House Robber

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given an integer array `nums` representing the amount of money
at each house, return the maximum amount you can rob without
robbing two adjacent houses.

Complexity
----------
Time  : O(n)
Space : O(n)

Key Idea
--------
Dynamic Programming:

    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

At each house, choose:
- Skip current house → dp[i-1]
- Rob current house  → dp[i-2] + nums[i]
"""

from __future__ import annotations
from typing import List


class Solution:
    """Compute maximum loot without robbing adjacent houses."""

    def rob(self, nums: List[int]) -> int:  # noqa: N802
        n: int = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp: List[int] = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([2, 7, 9, 3, 1]) == 12
    assert solution.rob([1, 5, 3, 2]) == 7
    assert solution.rob([2, 1, 1, 2]) == 4
    assert solution.rob([2, 7, 3, 1, 4, 2, 1, 8]) == 19

    print("✅ All tests passed successfully!")
