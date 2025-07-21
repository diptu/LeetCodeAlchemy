"""Test module for the max_sliding_window method in the Solution class."""

import pytest
from solution import Solution


@pytest.fixture
def solution():
    """
    Fixture to initialize the Solution class.

    Returns
    -------
    Solution
        An instance of the Solution class.
    """
    return Solution()


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([9, 11], 2, [11]),
        ([4, -2], 2, [4]),
        ([1, -1], 1, [1, -1]),
        ([7, 2, 4], 2, [7, 4]),
        ([1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]),
    ],
)
def testMaxSlidingWindow(solution, nums, k, expected):
    """
    Test the maxSlidingWindow function with various input cases.

    Parameters
    ----------
    solution : Solution
        Instance of the Solution class.
    nums : List[int]
        List of integers representing the input array.
    k : int
        Size of the sliding window.
    expected : List[int]
        Expected list of maximums for each window.

    Returns
    -------
    None
    """
    assert solution.maxSlidingWindow(nums, k) == expected
