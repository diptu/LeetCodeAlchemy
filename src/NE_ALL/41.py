"""
LeetCode #41: First Missing Positive

Author: Nazmul Alam Diptu
----------------------------------------

Problem
-------
Find the smallest missing positive integer in an unsorted array.

Constraints:
- O(n) time
- O(1) extra space

Key Idea
--------
1 <= answer <= len(nums) + 1
Use index marking to track presence.
"""

from __future__ import annotations
from typing import List


class Solution:
    """Solve the First Missing Positive problem using in-place hashing."""

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Return the smallest missing positive integer.

        Args:
            nums (List[int]): Input list of integers.

        Returns:
            int: Smallest missing positive integer.
        """
        size: int = len(nums)

        idx: int
        value: int
        target_idx: int

        # Step 1: Normalize values (ignore negatives & zeros)
        for idx in range(size):
            if nums[idx] <= 0:
                nums[idx] = 0

        # Step 2: Mark presence using index
        for idx in range(size):
            value = abs(nums[idx])

            if 1 <= value <= size:
                target_idx = value - 1

                if nums[target_idx] > 0:
                    nums[target_idx] *= -1
                elif nums[target_idx] == 0:
                    nums[target_idx] = -(size + 1)

        # Step 3: Find first missing positive
        for idx in range(size):
            if nums[idx] >= 0:
                return idx + 1

        return size + 1


# =============================================================================
# ✅ Unit Tests
# =============================================================================
def run_tests() -> None:
    """Run basic test cases."""
    solution: Solution = Solution()

    assert solution.firstMissingPositive([-2, -1, 0]) == 1
    assert solution.firstMissingPositive([1, 2, 0]) == 3
    assert solution.firstMissingPositive([3, 4, -1, 1]) == 2
    assert solution.firstMissingPositive([1, 2, 4, 5, 6, 3, 1]) == 7

    print("✅ All tests passed successfully!")


if __name__ == "__main__":
    run_tests()
