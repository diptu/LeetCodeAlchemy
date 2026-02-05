"""
LeetCode #2486. Append Characters to String to Make Subsequence

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given two strings `s` and `t`, return the minimum number of characters
that must be appended to the end of `s` so that `t` becomes a subsequence
of `s`.

Complexity
----------
Time:  O(n), where n = len(s)
Space: O(1)

Key Idea
--------
Two-pointer technique:
- Traverse `s` and `t` simultaneously
- Advance pointer in `t` only when characters match
- Remaining unmatched characters in `t` must be appended

Note
----
This is a greedy solution that finds the longest prefix of `t`
already present as a subsequence of `s`.
"""

from __future__ import annotations


class Solution:
    """Append characters to make `t` a subsequence of `s`."""

    def append_characters(self, s: str, t: str) -> int:
        """
        Return the minimum number of characters needed to append
        to `s` so that `t` becomes its subsequence.
        """
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t) - j


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.append_characters("coaching", "coding") == 4
    assert solution.append_characters("abcde", "a") == 0
    assert solution.append_characters("z", "abcde") == 5

    print("✅ All tests passed successfully!")
