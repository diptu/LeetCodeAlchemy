"""
LeetCode #1929 — Concatenation of Array

Author: Nazmul Alam Diptu
--------------------------------------------------------

Complexity
----------
Time  : O(n)
Space : O(n)

Key Idea
--------
Create a new array by appending the input array to itself.
"""

from __future__ import annotations
from typing import List


class Solution:
    """Generate the concatenation of an integer array with itself."""

    def getConcatenation(self, nums: List[int]) -> List[int]:  # noqa: N802
        """
        Return the concatenation of the given array with itself.

        Parameters
        ----------
        nums : List[int]
            Input list of integers.

        Returns
        -------
        List[int]
            Concatenated list: nums + nums.
        """
        N = len(nums)
        ans: List[int] = []

        for i in range(2 * N):
            idx = i % N
            ans.append(nums[idx])
        return ans


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert solution.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
    assert solution.getConcatenation([1, 4, 1, 2]) == [1, 4, 1, 2, 1, 4, 1, 2]
    assert solution.getConcatenation([22, 21, 20, 1]) == [22, 21, 20, 1, 22, 21, 20, 1]

    print("✅ All tests passed successfully!")
