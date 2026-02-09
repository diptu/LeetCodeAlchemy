"""
LeetCode #485. Max Consecutive Ones

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given a binary array `nums`, return the maximum number of consecutive 1s
in the array.

Complexity
----------
Time:  O(n), where n = len(nums)
Space: O(1)

Key Idea
--------
- Traverse the array once
- Maintain a running count of consecutive 1s
- Reset the count when a 0 is encountered
- Track the maximum seen so far

Note
----
This is a classic single-pass counter pattern.
"""

from __future__ import annotations
from typing import List


class Solution:
    """Compute the maximum number of consecutive 1s in a binary array."""

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:  # noqa: N802
        max_count: int = 0
        current_count: int = 0

        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

        return max_count


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2

    print("✅ All tests passed successfully!")
