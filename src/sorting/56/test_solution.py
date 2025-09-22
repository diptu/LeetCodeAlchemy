"""Pytest module for Solution.merge method."""

from typing import List
import pytest
from solution import Solution  # assumes the main code is saved as solution.py


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),  # touching intervals
        ([[1, 4]], [[1, 4]]),  # single interval
        ([[1, 4], [0, 2], [3, 5]], [[0, 5]]),  # nested intervals
        ([[1, 4], [5, 6]], [[1, 4], [5, 6]]),  # non-overlapping
        ([[1, 10], [2, 6], [3, 5], [7, 9]], [[1, 10]]),  # fully nested
        ([], []),  # empty input
    ],
)
def test_merge_intervals(intervals: List[List[int]], expected: List[List[int]]) -> None:
    """Test merge method with various interval inputs.

    Parameters
    ----------
    intervals : List[List[int]]
        List of intervals as [start, end].
    expected : List[List[int]]
        Expected list of merged intervals.
    """
    solution = Solution()
    result = solution.merge(intervals)
    assert result == expected


def test_single_interval() -> None:
    """Test merge method with only one interval."""
    solution = Solution()
    intervals = [[5, 7]]
    result = solution.merge(intervals)
    assert result == [[5, 7]]


def test_already_sorted_non_overlapping() -> None:
    """Test merge method with sorted, non-overlapping intervals."""
    solution = Solution()
    intervals = [[1, 2], [3, 4], [5, 6]]
    result = solution.merge(intervals)
    assert result == [[1, 2], [3, 4], [5, 6]]


def test_intervals_with_same_start() -> None:
    """Test merge method with intervals having the same start."""
    solution = Solution()
    intervals = [[1, 4], [1, 5], [1, 3]]
    result = solution.merge(intervals)
    assert result == [[1, 5]]
