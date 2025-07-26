"""Test module for the max_vowels method in the Solution class."""

import pytest
from solution import Solution


@pytest.fixture
def solution():
    """
    Fixture to create a Solution instance.

    Returns
    -------
    Solution
        An instance of the Solution class.
    """
    return Solution()


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
        ("rhythms", 4, 0),
        ("", 1, 0),
        ("bcbcbcbcbcbc", 2, 0),
        ("a", 1, 1),
        ("abcde", 5, 2),
        ("zazazazazaz", 3, 2),
        ("eouaeiouxyz", 5, 5),
    ],
)
def test_max_vowels(solution, s, k, expected):
    """
    Test max_vowels with various strings and window sizes.

    Parameters
    ----------
    solution : Solution
        An instance of the Solution class.
    s : str
        The input string to search for vowels in substrings.
    k : int
        The length of the substring window.
    expected : int
        The expected maximum number of vowels in any substring of length `k`.

    Returns
    -------
    None

    Time Complexity
    ---------------
    O(n), where n is the length of the string `s`.

    Space Complexity
    ----------------
    O(1), using constant space for counting and tracking vowels.
    """
    assert solution.max_vowels(s, k) == expected
