"""
LeetCode #32 — Longest Valid Parentheses

Author: Nazmul Alam Diptu
--------------------------------------------------------
This module implements two approaches for finding the length
of the longest valid (well-formed) parentheses substring.

Implementations
---------------
1. **Stack-based (Active)** → O(N) Time, O(N) Space
2. **Dynamic Programming (Commented)** → O(N) Time, O(N) Space
"""

from __future__ import annotations
from typing import List


# =============================================================================
# 🧠 Stack-Based Solution (Active)
# =============================================================================
class Solution:
    """
    Stack-based linear solution for the Longest Valid Parentheses problem.

    Key Idea
    --------
    Use a stack to store indices of unmatched '(' characters.

    - Initialize stack with [-1] as a base index.
    - For each character:
        - If '(', push its index.
        - If ')', pop from the stack.
            - If stack becomes empty → push current index (acts as new base).
            - Otherwise → valid substring = current index - top of stack.
    - Keep track of the maximum valid substring length found.

    Example
    -------
    >>> sol = Solution()
    >>> sol.longestValidParentheses(")()())")
    4
    Explanation: The longest valid substring is "()()".

    Complexity
    ----------
    Time  : O(N)
        Single pass through the string.
    Space : O(N)
        For the stack storing indices.
    """

    def longestValidParentheses(self, s: str) -> int:
        """
        Compute the length of the longest valid parentheses substring.

        Parameters
        ----------
        s : str
            Input string containing only '(' and ')'.

        Returns
        -------
        int
            Length of the longest valid parentheses substring.
        """
    

# =============================================================================
# 🧩 Alternative Dynamic Programming Solution (Commented Out)
# =============================================================================
"""
class Solution:
    '''
    Dynamic Programming approach for Longest Valid Parentheses.

    Key Idea
    ---------
    dp[i] = length of longest valid substring ending at index i.

    - If s[i] == ')' and s[i-1] == '(' → dp[i] = dp[i-2] + 2
    - If s[i] == ')' and s[i-1] == ')' and s[i - dp[i-1] - 1] == '('
        → dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]

    Complexity
    -----------
    Time  : O(N)
    Space : O(N)
    '''

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + (
                        dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0
                    )
                max_len = max(max_len, dp[i])

        return max_len
"""


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Basic test cases
    assert sol.longestValidParentheses("(()") == 2
    assert sol.longestValidParentheses(")()())") == 4
    assert sol.longestValidParentheses("") == 0
    assert sol.longestValidParentheses("()(()") == 2
    assert sol.longestValidParentheses("()(())") == 6

    print("✅ All tests passed successfully!")
