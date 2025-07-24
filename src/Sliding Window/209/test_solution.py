"""
pytest module for testing Solution.minSubArrayLen.

This module contains unit tests to verify correctness and edge-case
handling of the minimal subarray length algorithm.
"""

import pytest
from solution import Solution


@pytest.fixture(scope="module")
def solver() -> Solution:
    """Create a Solution instance for all test cases."""
    return Solution()


@pytest.mark.parametrize(
    "target, nums, expected",
    [
        (7, [2, 3, 1, 2, 4, 3], 2),  # example from documentation
        (4, [1, 4, 4], 1),  # single-element meets target
        (11, [1, 2, 3, 4, 5], 3),  # sum of last three = 12
        (5, [5], 1),  # single element equals target
        (100, [1, 2, 3], 0),  # no subarray meets target
    ],
)
def test_min_subarray_len_valid(solver, target, nums, expected):
    """Test valid inputs against expected minimal lengths."""
    result = solver.minSubArrayLen(target, nums)
    assert result == expected
