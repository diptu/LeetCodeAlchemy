"""Pytest module for testing the Maximum Subarray problem solution.

This test suite verifies correctness of the `max_sub_array` method from the
`Solution` class using multiple test cases, including edge cases.
"""

import pytest
from solution import Solution


@pytest.fixture
def solver():
    """Fixture to create a Solution instance."""
    return Solution()


def test_positive_numbers(solver):
    """Test with an array of positive integers."""
    nums = [1, 2, 3, 4]
    assert solver.max_sub_array(nums) == 10


def test_mixed_numbers(solver):
    """Test with a mix of positive and negative numbers."""
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert solver.max_sub_array(nums) == 6


def test_all_negative(solver):
    """Test with all negative integers."""
    nums = [-8, -3, -6, -2, -5, -4]
    assert solver.max_sub_array(nums) == -2


def test_single_element(solver):
    """Test with a single-element list."""
    nums = [5]
    assert solver.max_sub_array(nums) == 5


def test_large_input(solver):
    """Test with a large list to ensure efficiency."""
    nums = [1] * 10**6
    assert solver.max_sub_array(nums) == 10**6
