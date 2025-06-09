"""Tests for the anagram checker."""

import pytest
from solution import Solution


@pytest.fixture
def solution():
    """
    Fixture to provide a fresh instance of the Solution class.

    Returns
    -------
    Solution
        An instance of the Solution class.
    """
    return Solution()


def test_valid_anagram(solution):
    """
    Test that valid anagrams return True.

    Examples
    --------
    >>> solution = Solution()
    >>> solution.is_anagram("listen", "silent")
    True
    """
    assert solution.is_anagram("listen", "silent") is True
    assert solution.is_anagram("anagram", "nagaram") is True
    assert solution.is_anagram("mug", "gum") is True

    assert solution.is_anagram("a", "a") is True


def test_invalid_anagram(solution):
    """
    Test that non-anagrams return False.

    Examples
    --------
    >>> solution = Solution()
    >>> solution.is_anagram("rat", "car")
    False
    """
    assert solution.is_anagram("rat", "car") is False
    assert solution.is_anagram("hello", "helo") is False
    assert solution.is_anagram("a", "b") is False


def test_case_sensitivity(solution):
    """
    Test that anagram check is case-sensitive.

    Examples
    --------
    >>> solution = Solution()
    >>> solution.is_anagram("Listen", "silent")
    False
    """
    assert solution.is_anagram("Listen", "silent") is False
    assert solution.is_anagram("a", "A") is False


def test_empty_strings(solution):
    """
    Test that empty strings are considered anagrams of each other.

    Examples
    --------
    >>> solution = Solution()
    >>> solution.is_anagram("", "")
    True
    """
    assert solution.is_anagram("", "") is True
