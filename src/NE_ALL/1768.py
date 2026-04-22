"""
LeetCode #1768: Merge Strings Alternately

Author: Nazmul Alam Diptu
----------------------------------------

Problem
-------
Merge two strings by alternating characters.

If one string is longer, append the remaining characters.

Key Idea
--------
Use one index for both strings.
Store characters in a list, then join once at the end.
"""

from __future__ import annotations


class Solution:
    """Solve Merge Strings Alternately efficiently."""

    def merge_alternately(self, word1: str, word2: str) -> str:
        """
        Return merged string with alternating characters.

        Args:
            word1 (str): First string.
            word2 (str): Second string.

        Returns:
            str: Merged result.
        """
        result: list[str] = []

        len_word1: int = len(word1)
        len_word2: int = len(word2)
        index: int = 0

        while index < len_word1 or index < len_word2:
            if index < len_word1:
                result.append(word1[index])

            if index < len_word2:
                result.append(word2[index])

            index += 1

        return "".join(result)


# =============================================================================
# ✅ Unit Tests
# =============================================================================
def run_tests() -> None:
    """Run test cases."""
    solution: Solution = Solution()

    assert solution.merge_alternately("abc", "pqr") == "apbqcr"
    assert solution.merge_alternately("ab", "pqrs") == "apbqrs"
    assert solution.merge_alternately("abcd", "pq") == "apbqcd"

    print("✅ All tests passed successfully!")


if __name__ == "__main__":
    run_tests()
