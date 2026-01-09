"""
LeetCode #2405 — Optimal Partition of String

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given a string `s`, partition it into the minimum number of substrings
such that each substring contains only unique characters.

Return the number of such substrings.

Complexity
----------
Time  : O(n)
Space : O(1)   # At most 26 characters (lowercase English letters)

Key Idea
--------
Greedily build substrings from left to right.

- Maintain a set of characters in the current substring.
- If a character repeats, start a new substring.

This greedy strategy guarantees the minimum number of partitions.

Note
----
Using a set keeps membership checks O(1) and ensures linear-time
processing.
"""

from __future__ import annotations


class Solution:
    """Compute the minimum number of unique-character substrings."""

    def partitionString(self, s: str) -> int:  # noqa: N802
        """
        Return the minimum number of substrings with unique characters.

        Parameters
        ----------
        s : str
            Input string.

        Returns
        -------
        int
            Minimum number of partitions.
        """
        partitions: int = 1
        seen: set[str] = set()

        for char in s:
            if char in seen:
                partitions += 1
                seen.clear()

            seen.add(char)

        return partitions


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.partitionString("abacaba") == 4
    assert solution.partitionString("ssssss") == 6

    print("✅ All tests passed successfully!")
