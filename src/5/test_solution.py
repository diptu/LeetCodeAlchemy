import pytest
from solution import Solution


@pytest.fixture
def solution():
    """Fixture to create a Solution instance."""
    return Solution()


def test_longest_palindrome_basic(solution):
    """
    Test longestPalindrome on basic input strings.

    Examples
    --------
    >>> sol = Solution()
    >>> sol.longestPalindrome("babad")
    'bab'  # or 'aba'
    >>> sol.longestPalindrome("cbbd")
    'bb'
    """
    assert solution.longestPalindrome("babad") in ("bab", "aba")
    assert solution.longestPalindrome("cbbd") == "bb"
    assert solution.longestPalindrome("a") == "a"
    assert solution.longestPalindrome("ac") in ("a", "c")


def test_longest_palindrome_empty_and_single_char(solution):
    """
    Test edge cases: empty string and single character strings.
    """
    assert solution.longestPalindrome("") == ""
    assert solution.longestPalindrome("z") == "z"


def test_longest_palindrome_even_and_odd_length(solution):
    """
    Test strings with even and odd length palindromes.
    """
    assert solution.longestPalindrome("abba") == "abba"
    assert solution.longestPalindrome("racecar") == "racecar"


def test_longest_palindrome_no_palindrome(solution):
    """
    Test input strings with no palindrome longer than 1.
    """
    assert solution.longestPalindrome("abcde") in ("a", "b", "c", "d", "e")


def test_longest_palindrome_full_string(solution):
    """
    Test when entire string is a palindrome.
    """
    assert solution.longestPalindrome("aaaaaa") == "aaaaaa"
    assert solution.longestPalindrome("aba") == "aba"
