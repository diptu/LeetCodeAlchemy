"""
LeetCode #2390 — Removing Stars From a String

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given a string `s` consisting of lowercase letters and '*' characters,
remove each '*' along with the closest non-star character to its left.

It is guaranteed that for every '*' there exists a non-star character
to remove.

Complexity
----------
Time  : O(n)
Space : O(n)

Key Idea
--------
Use a stack (list) to process characters from left to right.

- Push letters onto the stack.
- On encountering '*', pop the most recent character.

Finally, join the stack to form the resulting string.

Note
----
This approach avoids repeated string concatenation and ensures
linear-time processing.
"""

from __future__ import annotations


class Solution:
    """Remove stars and their preceding characters from a string."""

    def removeStars(self, s: str) -> str:  # noqa: N802
        """
        Remove all '*' characters and the closest non-star character
        to the left of each '*'.

        Parameters
        ----------
        s : str
            Input string containing letters and '*'.

        Returns
        -------
        str
            Resulting string after all removals.
        """
        stack: list[str] = []

        for char in s:
            if char == "*":
                stack and stack.pop()  # pop if only non empty
            else:
                stack.append(char)

        return "".join(stack)


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.removeStars("leet**cod*e") == "lecoe"
    assert solution.removeStars("erase*****") == ""
    assert solution.removeStars("*****") == ""

    print("✅ All tests passed successfully!")
