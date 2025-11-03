"""
LeetCode #31 — Next Permutation

Author: Nazmul Alam Diptu
--------------------------------------------------------
This module implements the optimal algorithm to find the next
lexicographically greater permutation of a sequence of numbers.

Implementation
--------------
**In-place Next Permutation (Active)** → O(N) Time, O(1) Space
"""

from __future__ import annotations


# =============================================================================
# 🧠 In-place Permutation Algorithm (Active)
# =============================================================================
class Solution:
    """
    Efficient in-place solution for the Next Permutation problem.

    Key Idea
    --------
    To generate the next lexicographically greater permutation,
    we can follow a simple three-step logic:

    Steps
    -----
    1. **Find the Pivot**
        - Traverse from right to left to find the first index `i`
          such that `nums[i] < nums[i + 1]`.
        - This identifies the first decreasing element from the right.
        - If no such element exists, the array is in descending order
          → reverse it to get the smallest permutation.

    2. **Find the Next Greater Element**
        - From the right end, find the smallest element greater than `nums[i]`
          and swap it with `nums[i]`.

    3. **Reverse the Suffix**
        - Reverse the subarray `nums[i + 1:]` to make it ascending,
          giving the next permutation.

    Example
    -------
    >>> sol = Solution()
    >>> arr = [1, 2, 3]
    >>> sol.nextPermutation(arr)
    >>> arr
    [1, 3, 2]

    Complexity
    ----------
    Time  : O(N)
        Each step requires a single pass.
    Space : O(1)
        In-place transformation without extra data structures.
    """

    def nextPermutation(self, nums: list[int]) -> None:
        """
        Rearranges numbers into the next lexicographically greater permutation.

        Parameters
        ----------
        nums : List[int]
            List of integers to be rearranged.

        Returns
        -------
        None
            Modifies the input list in-place.
        """
        n = len(nums)
        i = n - 2

        # Step 1: Find pivot (first decreasing element from the right)
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the next greater element from the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Typical case
    nums = [1, 2, 3]
    sol.nextPermutation(nums)
    assert nums == [1, 3, 2]

    # Test 2: Reverse-sorted array → becomes smallest
    nums = [3, 2, 1]
    sol.nextPermutation(nums)
    assert nums == [1, 2, 3]

    # Test 3: Mixed case
    nums = [1, 1, 5]
    sol.nextPermutation(nums)
    assert nums == [1, 5, 1]

    # Test 4: Larger array
    nums = [1, 3, 2]
    sol.nextPermutation(nums)
    assert nums == [2, 1, 3]

    # Test 5: Single element (edge case)
    nums = [1]
    sol.nextPermutation(nums)
    assert nums == [1]

    print("✅ All tests passed successfully!")
