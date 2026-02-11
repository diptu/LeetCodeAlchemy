"""
LeetCode #1408. String Matching in an Array

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given an array of strings `words`, return all strings that are
a substring of another word in the array.

Complexity
----------
Time  : O(n^2 * m)
        n = number of words
        m = average word length
Space : O(m) for LPS array

Key Idea
--------
Use KMP string matching:
- For each pair (pattern, text)
- Build LPS for pattern
- Run KMP search
- If match found → add pattern to result
"""

from __future__ import annotations
from typing import List


class Solution:
    """Return all words that are substrings of another word using KMP."""

    def stringMatching(self, words: List[str]) -> List[str]:  # noqa: N802
        result: List[str] = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and self._kmp_search(words[i], words[j]):
                    result.append(words[i])
                    break

        return result

    # ---------------------------------------------------------
    # KMP SEARCH
    # ---------------------------------------------------------
    def _kmp_search(self, pattern: str, text: str) -> bool:
        """Return True if pattern exists in text using KMP."""
        if not pattern:
            return True

        lps = self._compute_lps(pattern)
        i = j = 0  # i -> text, j -> pattern

        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1

                if j == len(pattern):
                    return True
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return False

    # ---------------------------------------------------------
    # LPS ARRAY
    # ---------------------------------------------------------
    def _compute_lps(self, pattern: str) -> List[int]:
        """Compute Longest Prefix Suffix (LPS) array."""
        lps: List[int] = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.stringMatching(["mass", "as", "hero", "superhero"]) == [
        "as",
        "hero",
    ]

    assert solution.stringMatching(["leetcode", "et", "code"]) == ["et", "code"]

    print("✅ All tests passed successfully!")
