"""
LeetCode #3110 — Score of a String

Author: Nazmul Alam Diptu
--------------------------------------------------------

Complexity
----------
Time  : O(n)
Space : O(1)

Key Idea
--------
Iterate over adjacent characters and sum the absolute
difference of their ASCII values.
"""

from __future__ import annotations


class Solution:
    """Compute the score of a string based on adjacent character differences."""

    def scoreOfString(self, s: str) -> int:  # noqa: N802 (LeetCode naming)
        """
        Calculate the score of a string.

        The score is defined as the sum of absolute differences
        between the ASCII values of adjacent characters.

        Parameters
        ----------
        s : str
            Input string.

        Returns
        -------
        int
            Computed score of the string.
        """
        score: int = 0

        for left, right in zip(s, s[1:]):
            score += abs(ord(left) - ord(right))

        return score


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.scoreOfString("code") == 24
    assert solution.scoreOfString("neetcode") == 65
    assert solution.scoreOfString("hello") == 13
    assert solution.scoreOfString("zaz") == 50

    print("✅ All tests passed successfully!")
