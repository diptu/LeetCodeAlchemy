"""Module for validating balanced parentheses using a stack."""

from collections import deque


class Solution:
    """
    A class to validate if a string of brackets is well-formed.
    """

    def isValid(self, s: str) -> bool:
        """
        Check if the input string has valid matching brackets.

        Parameters
        ----------
        s : str
            A string consisting of '(', ')', '{', '}', '[' and ']'.

        Returns
        -------
        bool
            True if the brackets are balanced, False otherwise.
        """
        brackets = {")": "(", "}": "{", "]": "["}
        stack = deque()

        for char in s:
            if char in brackets:
                if not stack or stack[-1] != brackets[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    input_str = "()[]{}"
    result = solution.isValid(input_str)
    print(result)  # Expected: True
