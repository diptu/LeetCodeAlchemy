"""
LeetCode #33 — Search in Rotated Sorted Array

Author: Nazmul Alam Diptu
--------------------------------------------------------
This module implements an efficient binary search algorithm
to locate a target element in a rotated sorted array.

Implementation
--------------
**Binary Search (Active)** → O(log N) Time, O(1) Space
"""

from __future__ import annotations


# =============================================================================
# 🧠 Binary Search Solution (Active)
# =============================================================================
class Solution:
    """
    Optimized binary search solution for the Search in Rotated Sorted Array problem.

    Key Idea
    --------
    In a rotated sorted array, at least one half (either left or right)
    remains sorted at any given time. We can exploit this property to
    perform a modified binary search:

    Steps
    -----
    1. Initialize two pointers: left = 0, right = len(nums) - 1
    2. While left <= right:
        - Compute mid = (left + right) // 2
        - If nums[mid] == target → return mid
        - Determine which half is sorted:
            • If nums[left] <= nums[mid] → Left half is sorted
            • Else → Right half is sorted
        - Narrow down the search range based on where the target lies
    3. Return -1 if the target is not found.

    Example
    -------
    >>> sol = Solution()
    >>> sol.search([4,5,6,7,0,1,2], 0)
    4

    Complexity
    ----------
    Time  : O(log N)
        Each iteration halves the search space.
    Space : O(1)
        Only a few pointer variables are used.
    """

    def search(self, nums: list[int], target: int) -> int:
        """
        Search for a target value in a rotated sorted array.

        Parameters
        ----------
        nums : List[int]
            A list of unique integers sorted in ascending order and rotated.
        target : int
            The integer value to search for.

        Returns
        -------
        int
            Index of the target if found; otherwise, -1.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]

            # 🎯 Case 1: Found target
            if mid_val == target:
                return mid

            # 📈 Case 2: Left half is sorted
            if nums[left] <= mid_val:
                if nums[left] <= target < mid_val:
                    right = mid - 1  # target lies in left half
                else:
                    left = mid + 1  # target lies in right half

            # 📉 Case 3: Right half is sorted
            else:
                if mid_val < target <= nums[right]:
                    left = mid + 1  # target lies in right half
                else:
                    right = mid - 1  # target lies in left half

        return -1


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Basic test cases
    assert sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
    assert sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
    assert sol.search(nums=[1], target=0) == -1
    assert sol.search(nums=[1, 3], target=3) == 1
    assert sol.search(nums=[3, 1], target=3) == 0

    print("✅ All tests passed successfully!")
