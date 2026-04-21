"""
LeetCode #680: Valid Palindrome II

Author: Nazmul Alam Diptu
----------------------------------------

Problem
-------
Given a string s, return True if the string can become a palindrome
after deleting at most one character.

A palindrome reads the same forward and backward.

Constraints
-----------
- 1 <= len(s) <= 100_000
- s consists of lowercase English letters

Key Idea
--------
Use two pointers:

1. Compare characters from both ends.
2. If characters match, move inward.
3. On first mismatch, try:
   - Remove left character
   - Remove right character
4. Use slicing to check whether either remaining substring
   is a palindrome.
"""

from __future__ import annotations


class Solution:
    """Solve Valid Palindrome II using two pointers + slicing."""

    def valid_palindrome(self, text: str) -> bool:
        """
        Return True if text can become a palindrome
        after deleting at most one character.

        Args:
            text (str): Input string.

        Returns:
            bool: Whether a valid palindrome is possible.
        """
        left: int = 0
        right: int = len(text) - 1

        skip_left: str
        skip_right: str

        while left < right:
            if text[left] != text[right]:
                skip_left = text[left + 1 : right + 1]
                skip_right = text[left:right]

                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]

            left += 1
            right -= 1

        return True


# =============================================================================
# ✅ Unit Tests
# =============================================================================
def run_tests() -> None:
    """Run basic test cases."""
    solution: Solution = Solution()

    assert solution.valid_palindrome("aba") is True
    assert solution.valid_palindrome("abca") is True
    assert solution.valid_palindrome("abc") is False
    assert solution.valid_palindrome("deeee") is True
    assert solution.valid_palindrome("racecar") is True
    assert solution.valid_palindrome("abcdef") is False

    print("✅ All tests passed successfully!")


if __name__ == "__main__":
    run_tests()
