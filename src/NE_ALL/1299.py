"""
LeetCode #1299 — Replace Elements with Greatest Element on Right Side

Author: Nazmul Alam Diptu
--------------------------------------------------------

Complexity
----------
Time  : O(n)
Space : O(1)

Key Idea
--------
Traverse the array from right to left while tracking the
maximum value seen so far.
"""

from __future__ import annotations
from typing import List


class Solution:
    """Replace each element with the greatest element to its right."""

    def replaceElements(self, arr: List[int]) -> List[int]:  # noqa: N802
        """
        Replace elements with the maximum value on their right.

        The last element is always replaced with -1.

        Parameters
        ----------
        arr : List[int]
            Input list of integers.

        Returns
        -------
        List[int]
            Modified list with replaced values.
        """
        max_right: int = -1

        for index in range(len(arr) - 1, -1, -1):
            current: int = arr[index]
            arr[index] = max_right
            max_right = max(max_right, current)

        return arr


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
    assert solution.replaceElements([400]) == [-1]
    assert solution.replaceElements([2, 4, 5, 3, 1, 2]) == [5, 5, 3, 2, 2, -1]
    assert solution.replaceElements([3, 3]) == [3, -1]

    print("✅ All tests passed successfully!")
