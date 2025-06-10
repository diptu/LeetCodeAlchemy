"""Test suite for the twoSum method in the Solution class."""

import pytest
from solution import Solution


@pytest.fixture
def solution():
    """Fixture to create a Solution instance."""
    return Solution()


def test_valid_pair_found(solution):
    """
    Test that a valid pair is correctly returned.

    Checks if the method returns correct indices when a valid pair exists.
    """
    assert sorted(solution.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(solution.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(solution.twoSum([3, 3], 6)) == [0, 1]
    assert sorted(solution.twoSum([1, 5, 3, 4], 9)) == [1, 3]


def test_with_negative_numbers(solution):
    """
    Test the method with negative integers.

    Ensures that the method handles negative values correctly.
    """
    assert sorted(solution.twoSum([-3, 4, 3, 90], 0)) == [0, 2]
