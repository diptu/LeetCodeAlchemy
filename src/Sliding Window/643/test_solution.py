# -*- coding: utf-8 -*-
"""
pytest module for testing Solution.find_max_average.

This module contains unit tests to verify correctness and
edge-case handling of the sliding-window maximum average algorithm.
"""

import pytest
from solution import Solution


@pytest.fixture(scope="module")
def solver() -> Solution:
    """Create a Solution instance for use in all test cases."""
    return Solution()


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),  # example from documentation
        ([5, 5, 5, 5, 5], 2, 5.0),  # all elements equal
        ([0, -1, -2, -3], 3, -1.0),  # negative numbers
        ([10], 1, 10.0),  # single element window
        ([4, 2, 1, 3, 5], 5, 3.0),  # window equals array length
    ],
)
def test_find_max_average_valid(solver, nums, k, expected):
    """Test valid inputs against expected maximum average."""
    result = solver.findMaxAverage(nums, k)
    assert pytest.approx(result, rel=1e-6) == expected
