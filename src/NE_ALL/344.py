"""
LeetCode #344: Reverse String

Author: Nazmul Alam Diptu
----------------------------------------

Problem
-------
Reverse a list of characters in-place.

Constraints:
- Modify the input list directly  O(n)
- O(1) extra space

Key Idea
--------
Use two pointers:
- One from the start
- One from the end
Swap until they meet
"""

from __future__ import annotations
from typing import List


class Solution:
    """Solve the Reverse String problem using two-pointer technique."""

    def reverse_string(self, chars: List[str]) -> None:
        """
        Reverse the list of characters in-place.

        Args:
            chars (List[str]): List of single-character strings.

        Returns:
            None
        """
        size: int = len(chars)

        left: int
        right: int

        for left in range(size // 2):
            right = size - 1 - left
            chars[left], chars[right] = chars[right], chars[left]


# =============================================================================
# ✅ Unit Tests
# =============================================================================
def run_tests() -> None:
    """Run basic test cases."""
    solution: Solution = Solution()

    chars1: List[str] = ["h", "e", "l", "l", "o"]
    solution.reverse_string(chars1)
    assert chars1 == ["o", "l", "l", "e", "h"]

    chars2: List[str] = ["H", "a", "n", "n", "a", "h"]
    solution.reverse_string(chars2)
    assert chars2 == ["h", "a", "n", "n", "a", "H"]

    print("✅ All tests passed successfully!")


if __name__ == "__main__":
    run_tests()
