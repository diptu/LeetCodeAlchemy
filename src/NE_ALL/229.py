"""
LeetCode #229. Majority Element II

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given an integer array `nums`, return all elements that appear
more than ⌊ n/3 ⌋ times.

Complexity
----------
Time  : O(n)
Space : O(1)

Key Idea
--------
Boyer-Moore Voting Algorithm (extended):

- There can be at most 2 elements appearing more than n/3 times
- First pass: find potential candidates
- Second pass: verify their counts
"""

from __future__ import annotations
from typing import List


class Solution:
    """Find all elements appearing more than ⌊ n/3 ⌋ times."""

    def majorityElement(self, nums: List[int]) -> List[int]:  # noqa: N802
        # Step 1: Find candidates
        candidate1: int | None = None
        candidate2: int | None = None
        count1: int = 0
        count2: int = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidates
        result: List[int] = []
        n: int = len(nums)

        if nums.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > n // 3:
            result.append(candidate2)

        return result


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.majorityElement([3, 1, 3]) == [3]
    assert solution.majorityElement([1]) == [1]
    assert sorted(solution.majorityElement([1, 2])) == [1, 2]
    assert sorted(solution.majorityElement([1, 1, 1, 3, 3, 2, 2, 2])) == [1, 2]

    print("✅ All tests passed successfully!")
