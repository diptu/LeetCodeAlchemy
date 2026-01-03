"""
LeetCode #424 — Longest Repeating Character Replacement

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given a string `s` and an integer `k`, return the length of the
longest substring that can be obtained by replacing at most `k`
characters so that all characters in the substring are the same.

Complexity
----------
Time  : O(n)
Space : O(m)   # m = number of distinct characters in the window

Key Idea
--------
Use a sliding window with character frequency tracking.

Maintain a window such that:
    window_size - max_character_frequency <= k

If the window becomes invalid, shrink it from the left until the
constraint is satisfied again. Track the maximum valid window size.

Note
----
The maximum character frequency is not decreased when the window
shrinks. This may temporarily overestimate the frequency, but it
does not affect correctness and ensures O(n) time complexity.
"""

from __future__ import annotations
from typing import Dict


class Solution:
    """Find the longest substring with at most k replacements."""

    def characterReplacement(self, s: str, k: int) -> int:  # noqa: N802
        """
        Return the length of the longest repeating-character substring
        after at most `k` replacements.
        """
        freq: Dict[str, int] = {}
        left: int = 0
        max_freq: int = 0
        max_length: int = 0

        for right, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1
            max_freq = max(max_freq, freq[char])

            # Shrink window if invalid
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Window is valid here
            max_length = max(max_length, right - left + 1)

        return max_length


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.characterReplacement("ABAB", 2) == 4
    assert solution.characterReplacement("AABABBA", 1) == 4

    print("✅ All tests passed successfully!")
