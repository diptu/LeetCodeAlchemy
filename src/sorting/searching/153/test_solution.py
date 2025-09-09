"""Pytest for Solution.findMin function."""

from typing import List
import pytest
from solution import Solution  # Assuming your main code is in solution.py


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([11, 13, 15, 17], 11),  # Non-rotated array
        ([15, 17, 11, 13], 11),  # Rotated array
        ([2, 3, 4, 5, 1], 1),  # Rotated with min at end
        ([1], 1),  # Single element
        ([3, 1, 2], 1),  # Small rotated array
        ([5, 6, 1, 2, 3, 4], 1),  # Rotated with multiple elements
    ],
)
def test_findMin(nums: List[int], expected: int) -> None:
    """Test findMin with various rotated and non-rotated arrays.

    Args:
        nums (List[int]): Input rotated sorted array.
        expected (int): Expected minimum value.
    """
    solution = Solution()
    result = solution.findMin(nums)
    assert result == expected


def test_single_element() -> None:
    """Test findMin with a single-element array."""
    solution = Solution()
    nums = [42]
    result = solution.findMin(nums)
    assert result == 42


def test_sorted_array() -> None:
    """Test findMin with a fully sorted (non-rotated) array."""
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    result = solution.findMin(nums)
    assert result == 1
