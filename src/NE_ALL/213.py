"""
LeetCode #213. House Robber II

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
You are given an integer array `nums` representing the amount of money
in each house arranged in a circle.

You cannot rob two adjacent houses, and the first and last houses
are also adjacent.

Return the maximum amount of money you can rob.

Complexity
----------
Time  : O(n)
Space : O(n)

Key Idea
--------
Since houses form a circle, we cannot rob both the first and last house.

So we split into two cases:
1. Rob houses from index 0 to n-2 (exclude last)
2. Rob houses from index 1 to n-1 (exclude first)

The answer is the maximum of these two linear robberies.
"""

from __future__ import annotations
from typing import List


class Solution:
    """Compute maximum loot in circular house arrangement."""

    def rob(self, nums: List[int]) -> int:  # noqa: N802
        n: int = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        return max(
            self._rob_linear(nums[:-1]),  # exclude last
            self._rob_linear(nums[1:]),  # exclude first
        )

    def _rob_linear(self, nums: List[int]) -> int:
        """Standard House Robber I (linear version)."""
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

    assert solution.rob([2, 3, 2]) == 3
    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([1, 2, 3]) == 3
    assert solution.rob([9, 1, 2, 9]) == 11

    print("✅ All tests passed successfully!")
