"""
LeetCode #322. Coin Change

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given an array of coin denominations `coins` and an integer `amount`,
return the minimum number of coins required to make up that amount.

If the amount cannot be formed, return -1.

Complexity
----------
Time  : O(n * amount)
Space : O(amount)

Key Idea
--------
Dynamic Programming.

Let:
    dp[i] = minimum number of coins needed to make amount i

Transition:
    dp[i] = min(dp[i], dp[i - coin] + 1)

Build the solution bottom-up from 0 → amount.
"""

from __future__ import annotations
from typing import List


class Solution:
    """Compute the minimum number of coins needed to form a given amount."""

    def coinChange(self, coins: List[int], amount: int) -> int:  # noqa: N802
        if amount == 0:
            return 0

        dp: List[int] = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.coinChange([1, 2, 5], 11) == 3
    assert solution.coinChange([2], 3) == -1
    assert solution.coinChange([1], 0) == 0

    print("✅ All tests passed successfully!")
