"""
Unit tests for the Solution class's isPalindrome method using pytest.

These tests verify that the method correctly identifies integer palindromes.
"""

import pytest
from solution import Solution


@pytest.mark.parametrize(
    "input_val,expected",
    [
        (121, True),
        (-121, False),
        (0, True),
        (10, False),
    ],
)
def test_is_palindrome(input_val, expected):
    """
    Test the isPalindrome method of the Solution class.

    Parameters
    ----------
    input_val : int
        The integer to check.

    expected : bool
        The expected result.

    Asserts
    -------
    That isPalindrome returns the expected boolean result.
    """
    solution = Solution()
    assert solution.isPalindrome(input_val) == expected
