import pytest
from solution import Solution


@pytest.fixture
def solver():
    """Fixture to provide a reusable Solution instance."""
    return Solution()


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("abcabcbb", 3),  # "abc"
        ("bbbbb", 1),  # "b"
        ("pwwkew", 3),  # "wke"
        ("", 0),  # Empty string
        ("a", 1),  # Single character
        ("ab", 2),  # All unique
        ("dvdf", 3),  # "vdf"
        ("abba", 2),  # "ab" or "ba"
    ],
)
def test_length_of_longest_substring(solver, input_str, expected):
    """
    Test the length_of_longest_substring method with various inputs.

    Parameters
    ----------
    solver : Solution
        Instance of the Solution class (from fixture).
    input_str : str
        Input string to test.
    expected : int
        Expected length of the longest unique-character substring.
    """
    result = solver.lengthOfLongestSubstring(input_str)
    assert result == expected
