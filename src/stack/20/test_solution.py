"""
Pytest unit tests for Solution.is_valid method.
"""

import pytest
from solution import Solution


@pytest.fixture
def solution():
    """
    Fixture to provide a Solution instance.
    """
    return Solution()


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("[", False),
        ("]", False),
        ("{{{{", False),
        ("([]{})", True),
    ],
)
def test_is_valid(solution, input_str, expected):
    """
    Test Solution.is_valid with various bracket strings.

    Parameters
    ----------
    solution : Solution
        Fixture providing an instance of the Solution class.
    input_str : str
        The bracket string to test.
    expected : bool
        Expected result indicating whether the input is valid.
    """
    assert solution.isValid(input_str) is expected
