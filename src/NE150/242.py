"""
Valid Anagram Problem (LeetCode #242)

Author: Nazmul Alam Diptu
-----------------------------------------
This module provides two implementations of the "Valid Anagram" problem.

Problem Summary:
----------------
Given two strings `s` and `t`, determine whether they are anagrams of each other.
Two strings are anagrams if they contain the same characters with the same
frequency, regardless of order.

Goal:
-----
Return `True` if the two strings are anagrams, otherwise `False`.

Implementations:
----------------
1. **Counter-based Solution (Optimal)** → O(N), O(1)
2. **Sorting-based Solution (Concise)** → O(N log N), O(1)

Only the optimal Counter-based solution is active by default.
"""

from __future__ import annotations

from collections import Counter

# =============================================================================
# 🧠 Optimal O(N) Using collections.Counter
# =============================================================================


class Solution:
    """
    Optimal O(N) solution for the Valid Anagram problem.

    Key Idea
    --------
    Use Python’s built-in `collections.Counter` to count the frequency of
    each character in both strings and compare the two resulting counters.

    If both have identical counts for every character, they are anagrams.

    Example
    -------
    >>> sol = Solution()
    >>> sol.isAnagram("anagram", "nagaram")
    True
    >>> sol.isAnagram("rat", "car")
    False

    Complexity
    ----------
    Time  : O(N)
        Counting characters once per string.
    Space : O(1)
        Constant space since there are only 26 lowercase letters.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        """Return True if two strings are anagrams, else False."""
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


# =============================================================================
# 🧩 Alternative Sorting-based Implementation
# =============================================================================
"""
class Solution:
    '''
    Sorting-based Solution (O(N log N))

    Key Idea
    ---------
    Sort both strings and compare them. If they are identical after sorting,
    the strings are anagrams.

    Example
    --------
    >>> sol = Solution()
    >>> sol.isAnagram("anagram", "nagaram")
    True
    >>> sol.isAnagram("rat", "car")
    False

    Complexity
    -----------
    Time  : O(N log N)
        Due to sorting both strings.
    Space : O(1)
        Ignoring sorting buffer overhead.
    '''

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
"""


# =============================================================================
# ✅ Unit Tests
# =============================================================================

if __name__ == "__main__":
    sol = Solution()

    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False

    print("✅ All tests passed successfully!")
