"""
LeetCode #14 — Longest Common Prefix

Author: Nazmul Alam Diptu
--------------------------------------------------------

Implementations
---------------
1. **Sorting-Based (Optimized)** → O(N log N) Time, O(1) Space

Key Idea
--------
Instead of comparing every word pair, we:
1. Sort the list of strings alphabetically.
2. Only compare characters between the **first** and **last** strings.
   - These two strings represent the minimum and maximum lexicographically.
   - Their shared prefix is guaranteed to be the prefix shared by all.
"""

from __future__ import annotations


class Solution:
    """Optimized, typed, and pylint-clean implementation of LCP."""

    def longestCommonPrefix(self, strs: list[str]) -> str:  # noqa: N802
        """
        Compute the longest common prefix among a list of strings.

        Steps
        -----
        1. Sort the list of input strings.
        2. Compare characters between the first and last strings until mismatch.

        Parameters
        ----------
        strs : List[str]
            The list of strings for which we compute the longest common prefix.

        Returns
        -------
        str
            The longest common prefix. Empty string if no common prefix exists.
        """
        if not strs:
            return ""

        strs.sort()
        first, last = strs[0], strs[-1]

        prefix_chars: list[str] = []
        limit = min(len(first), len(last))

        for i in range(limit):
            if first[i] != last[i]:
                break
            prefix_chars.append(first[i])

        return "".join(prefix_chars)


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert sol.longestCommonPrefix(["a"]) == "a"
    assert (
        sol.longestCommonPrefix(["interspecies", "interstellar", "interstate"])
        == "inters"
    )

    print("✅ All tests passed successfully!")
