"""
LeetCode #392 — Is Subsequence

Author: Nazmul Alam Diptu
--------------------------------------------------------

Complexity
----------
Time  : O(n)
Space : O(1)

Key Idea
--------
Use two pointers to scan both strings from left to right
and greedily match characters.
"""

from __future__ import annotations


class Solution:
    """Check whether one string is a subsequence of another."""

    def isSubsequence(self, s: str, t: str) -> bool:  # noqa: N802
        """
        Determine if `s` is a subsequence of `t`.

        Parameters
        ----------
        s : str
            Candidate subsequence string.
        t : str
            Target string.

        Returns
        -------
        bool
            True if `s` is a subsequence of `t`, otherwise False.
        """
        s_index: int = 0

        for char in t:
            if s_index == len(s):
                break

            if char == s[s_index]:
                s_index += 1

        return s_index == len(s)


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.isSubsequence("abc", "ahbgdc") is True
    assert solution.isSubsequence("axc", "ahbgdc") is False
    assert solution.isSubsequence("node", "neetcode") is True
    # Edge cases
    assert solution.isSubsequence("", "ahbgdc") is True
    assert solution.isSubsequence("b", "abc") is True

    print("✅ All tests passed successfully!")
