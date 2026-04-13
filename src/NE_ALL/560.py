"""
LeetCode #560. Subarray Sum Equals K

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given an integer array `nums` and an integer `k`,
return the total number of subarrays whose sum equals `k`.

Complexity
----------
Time  : O(n)
Space : O(n)

Key Idea
--------
Prefix Sum + Hash Map

- Let `prefix_sum[i]` be the sum of elements from index 0 to i
- For current sum `curr`, we want:
      curr - previous_sum = k
  => previous_sum = curr - k

- Use a hashmap to store frequency of prefix sums

Example:
    nums = [1,1,1], k = 2
    prefix sums = [1,2,3]

    When curr = 2:
        2 - 2 = 0 → found in map → count++

"""

from __future__ import annotations
from typing import Dict, List


class Solution:
    """Count number of subarrays with sum equal to k."""

    def subarraySum(self, nums: List[int], k: int) -> int:  # noqa: N802
        count: int = 0
        current_sum: int = 0
        prefix_count: Dict[int, int] = {0: 1}

        for num in nums:
            current_sum += num
            target: int = current_sum - k

            count += prefix_count.get(target, 0)
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return count


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.subarraySum([1, 1, 1], 2) == 2
    assert solution.subarraySum([1, 2, 3], 3) == 2
    assert solution.subarraySum([2, -1, 1, 2], 2) == 4
    assert solution.subarraySum([4, 4, 4, 4, 4, 4], 4) == 6

    print("✅ All tests passed successfully!")
