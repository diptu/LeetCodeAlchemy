"""Unit tests for the groupAnagrams method in the Solution class."""

import pytest
from solution import Solution


@pytest.fixture
def solution():
    """
    Fixture for initializing the Solution class.

    Returns
    -------
    Solution
        An instance of the Solution class.
    """
    return Solution()


@pytest.mark.parametrize(
    "input_strs, expected_groups",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc", "bca", "cab", "xyz", "zyx"], [["abc", "bca", "cab"], ["xyz", "zyx"]]),
    ],
)
def test_groupAnagrams(solution, input_strs, expected_groups):
    """
    Test the groupAnagrams method with various input scenarios.

    Parameters
    ----------
    solution : Solution
        Fixture providing an instance of the Solution class.
    input_strs : List[str]
        List of input strings to group.
    expected_groups : List[List[str]]
        Expected grouped anagram lists (order within groups may vary).
    """
    result = solution.groupAnagrams(input_strs)

    # Convert inner lists to sets for unordered comparison
    result_sets = [set(group) for group in result]
    expected_sets = [set(group) for group in expected_groups]

    assert sorted(result_sets) == sorted(expected_sets)
