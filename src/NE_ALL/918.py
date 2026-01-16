"""
LeetCode #918 — Maximum Sum Circular Subarray

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given a circular integer array `nums`, return the maximum possible sum
of a non-empty subarray of `nums`.

A circular array allows subarrays to wrap from the end of the array
to the beginning.

Complexity
----------
Time  : O(n)
Space : O(1)

Key Idea
--------
Kadane’s Algorithm with a circular twist:

1. Apply standard Kadane to find the maximum subarray sum.
2. Apply inverted Kadane to find the minimum subarray sum.
3. The maximum circular sum is:
       total_sum - minimum_subarray_sum

Edge Case
---------
If all numbers are negative, the circular case is invalid.
Return the maximum element instead.
"""

from __future__ import annotations
from typing import List


class Solution:
    """Compute the maximum subarray sum in a circular array."""

    def maxSubarraySumCircular(self, nums: List[int]) -> int:  # noqa: N802
        """
        Return the maximum sum of a non-empty subarray in a circular array.

        Parameters
        ----------
        nums : List[int]
            Circular list of integers.

        Returns
        -------
        int
            Maximum subarray sum.
        """
        max_sum = min_sum = nums[0]
        current_max = current_min = 0
        total_sum = 0

        for num in nums:
            current_max = max(num, current_max + num)
            current_min = min(num, current_min + num)

            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)

            total_sum += num

        # If all values are negative, circular case is invalid
        if max_sum <= 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.maxSubarraySumCircular(nums=[1, -2, 3, -2]) == 3
    assert solution.maxSubarraySumCircular(nums=[5, -3, 5]) == 10
    assert solution.maxSubarraySumCircular(nums=[-3, -2, -3]) == -2
    assert solution.maxSubarraySumCircular(nums=[3, -1, 2, -1]) == 4

    print("✅ All tests passed successfully!")
